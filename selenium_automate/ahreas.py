import os
import re
import sys
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# =========================
# CONFIG
# =========================
URL = "https://ahreas.jaime.com.br/administracaoweb/"
USUARIO = "SEU_USUARIO"
SENHA = "SUA_SENHA"

CHROMIUM_BIN = "/snap/bin/chromium"
VERSION_RE = re.compile(r"\b\d+\.\d+\.\d+\.\d+\b")  # ex: 1.2026.0126.0004

# timeouts
PAGE_READY_TIMEOUT = 40
STEP_TIMEOUT = 20
TOTAL_TIMEOUT_SECONDS = 120  # tempo máximo total do robô


# =========================
# UTILS
# =========================
def log(msg: str):
    print(msg, flush=True)


def dump_debug(driver, prefix="debug"):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("debug", exist_ok=True)

    html_path = f"debug/{prefix}_{ts}.html"
    png_path = f"debug/{prefix}_{ts}.png"

    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        driver.save_screenshot(png_path)
    except Exception as e:
        log(f"[DEBUG] Falha ao salvar debug: {e}")
        return

    log(f"[DEBUG] URL atual: {driver.current_url}")
    log(f"[DEBUG] Title: {driver.title}")
    log(f"[DEBUG] HTML salvo em: {html_path}")
    log(f"[DEBUG] Screenshot salvo em: {png_path}")


def criar_driver():
    options = Options()
    options.binary_location = CHROMIUM_BIN

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")

    # snap/headless: perfil em /tmp
    options.add_argument("--user-data-dir=/tmp/chrome-data")
    options.add_argument("--disk-cache-dir=/tmp/chrome-cache")

    # estabilidade
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-features=VizDisplayCompositor")

    # anti-bloqueio leve
    options.add_argument("--lang=pt-BR")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)

    try:
        driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    except Exception:
        pass

    return driver


def get_body_text(driver) -> str:
    return driver.execute_script("return document.body.innerText") or ""


def try_get_version(driver) -> str | None:
    txt = get_body_text(driver)
    m = VERSION_RE.search(txt)
    return m.group(0) if m else None


def click_by_text_js(driver, text: str):
    driver.execute_script(
        """
        const targetText = arguments[0];
        const els = Array.from(document.querySelectorAll('a,button,div,span'));
        function isVisible(el){
          const r = el.getBoundingClientRect();
          const s = window.getComputedStyle(el);
          return r.width > 0 && r.height > 0 && s.display !== 'none' && s.visibility !== 'hidden';
        }
        const el = els.find(e => isVisible(e) && (e.innerText || '').trim() === targetText);
        if (el) el.click();
        """,
        text
    )


def wait_login_fields(driver, timeout=8):
    w = WebDriverWait(driver, timeout)
    user = w.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[id$='idusuario'], input[name$='idusuario']")))
    pwd = w.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[id$='idpassword'], input[name$='idpassword']")))
    return user, pwd


def try_login(driver) -> bool:
    """
    Retorna True se executou login, False se não encontrou tela de login.
    """
    # tenta aparecer login no DOM principal
    try:
        user, pwd = wait_login_fields(driver, timeout=6)
    except TimeoutException:
        # tenta em iframes (caso carregue dentro)
        frames = driver.find_elements(By.TAG_NAME, "iframe")
        for fr in frames:
            driver.switch_to.default_content()
            try:
                driver.switch_to.frame(fr)
                user, pwd = wait_login_fields(driver, timeout=3)
                break
            except TimeoutException:
                continue
        else:
            driver.switch_to.default_content()
            return False  # sem login no DOM nem em iframe

    # encontrou: faz login
    log("[INFO] Tela de login encontrada. Preenchendo credenciais...")
    user.clear()
    pwd.clear()
    user.send_keys(USUARIO)
    pwd.send_keys(SENHA)

    # botão entrar
    btns = driver.find_elements(
        By.CSS_SELECTOR, "button#goLogin_btnEntrar, button[data-submit='goLogin_hbLogin']")
    if btns:
        btn = btns[0]
    else:
        btn = driver.find_element(By.XPATH, "//button[contains(., 'Entrar')]")

    btn.click()

    # volta para default (se estiver em iframe) antes de esperar sumir
    driver.switch_to.default_content()

    # espera sair da tela de login (sumir campo usuário)
    WebDriverWait(driver, STEP_TIMEOUT).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR,
                      "input[id$='idusuario'], input[name$='idusuario']")) == 0
    )
    log("[INFO] Login aparenta ter avançado.")
    return True


# =========================
# MAIN
# =========================
def main():
    start = time.time()
    driver = criar_driver()

    try:
        log("[INFO] Abrindo URL...")
        driver.get(URL)

        WebDriverWait(driver, PAGE_READY_TIMEOUT).until(
            lambda d: d.execute_script("return document.readyState") in (
                "interactive", "complete")
        )
        log(
            f"[INFO] Página carregada. Title='{driver.title}' URL='{driver.current_url}'")

        # 1) tenta pegar versão direto
        v = try_get_version(driver)
        if v:
            log(f"VERSÃO: {v}")
            return

        # 2) tenta abrir algum fluxo (às vezes o login fica atrás de um botão)
        log("[INFO] Versão não encontrada de cara. Tentando abrir 'Entrar' / 'Módulo'...")
        click_by_text_js(driver, "Entrar")
        time.sleep(1)
        click_by_text_js(driver, "Módulo")
        time.sleep(1)

        # 3) tenta login (se tela existir)
        executed_login = False
        try:
            executed_login = try_login(driver)
        except Exception as e:
            dump_debug(driver, "login_error")
            raise RuntimeError(f"Erro durante login: {e}")

        # 4) tenta versão depois do fluxo
        v = try_get_version(driver)
        if v:
            log(f"VERSÃO: {v}")
            return

        # 5) sem versão: salva debug sempre
        dump_debug(driver, "version_not_found")
        state = "com tentativa de login" if executed_login else "sem tela de login (não encontrada)"
        raise RuntimeError(
            f"Não encontrei a versão no texto da página ({state}). Veja ./debug.")

    finally:
        driver.quit()
        elapsed = int(time.time() - start)
        log(f"[INFO] Finalizado em {elapsed}s.")


if __name__ == "__main__":
    # garante que sempre termina
    try:
        main()
    except Exception as e:
        print(f"[ERRO] {e}", file=sys.stderr, flush=True)
        sys.exit(1)
