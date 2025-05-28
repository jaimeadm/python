#!/usr/bin/python3
"""
Script: jrenova.py
Criado em: 27/03/2025
Atualizado em: 28/03/2025
Autor: Alan M O Silva
Descricao: Faz leitura de PDFs na pasta "/mnt/jrenova", separa paginas (se necessario), extrai CNPJs da pasta papelada e envia por e-mail.
"""
__version__ = "1.0.1"

import fitz
import os
import smtplib
import mimetypes
import time
import shutil
import re
from pathlib import Path
from email.message import EmailMessage
from datetime import datetime

# Arquivo de log
LOG_PATH = "jrenova.log"

# Configuracao do e-mail
EMAIL_REMETENTE = "jrenova@jaime.com.br"
EMAIL_LOGIN = "AKIAVA6I6DDD76RKVPJV"
EMAIL_SENHA = "BJvvlO7tblcWijPfxiANMi5FKvscEHWqZhlBlCB7rhJy"
EMAIL_DESTINATARIO = "alan.silva@jaime.com.br"
SMTP_SERVIDOR = "email-smtp.sa-east-1.amazonaws.com"
SMTP_PORTA = 587

# Função para gerar log


def log(msg):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    linha = f"{agora} | {msg}"
    print(linha)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(linha + "\n")


# Diretorios
base_dir = "jrenova"
output_dir_paginas = os.path.join(base_dir, "paginas_separadas")
os.makedirs(output_dir_paginas, exist_ok=True)

# Função para envio de e-mail


def enviar_email(arquivo):
    msg = EmailMessage()
    msg['Subject'] = "jrenova - Documento Gerado"
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINATARIO
    msg.set_content(
        f"Ola, segue o arquivo {os.path.basename(arquivo)} em anexo.")

    mime_tipo, _ = mimetypes.guess_type(arquivo)
    if mime_tipo is None:
        mime_tipo = "application/octet-stream"
    tipo_principal, tipo_sub = mime_tipo.split("/")

    with open(arquivo, "rb") as f:
        msg.add_attachment(f.read(), maintype=tipo_principal,
                           subtype=tipo_sub, filename=os.path.basename(arquivo))

    with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as server:
        server.starttls()
        server.login(EMAIL_LOGIN, EMAIL_SENHA)
        server.send_message(msg)

    log(f"E-mail enviado para {EMAIL_DESTINATARIO} com o arquivo {arquivo}")
    time.sleep(5)  # Pausa de 5 segundos apos cada envio

# Função para mostrar os dados dos PDFs na pasta papelada buscando CNPJ com ER


def extrair_cnpjs_de_pdfs(diretorio):
    padrao_cnpj = re.compile(r'\b\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}\b')

    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        if nome_arquivo.lower().endswith(".pdf") and os.path.isfile(caminho_arquivo):
            try:
                pdf = fitz.open(caminho_arquivo)
                for pagina in pdf:
                    linhas = pagina.get_text("blocks")
                    linhas.sort(key=lambda b: (b[1], b[0]))
                    for bloco in linhas:
                        linha = bloco[4].strip()
                        cnpj_match = padrao_cnpj.search(linha)
                        if cnpj_match:
                            cnpj = cnpj_match.group()
                            colunas = linha.split()
                            codigo = colunas[0] if len(colunas) > 0 else "N/A"
                            condominio = colunas[1] if len(colunas) > 1 else ""
                            log(f"[{nome_arquivo}] Codigo: {codigo} | Condominio: {condominio} | CNPJ: {cnpj}")
                pdf.close()
            except Exception as e:
                log(f"Erro ao processar {nome_arquivo}: {e}")


# Processamento dos PDFs
arquivos_pdf = [
    f for f in os.listdir(base_dir)
    if f.lower().endswith(".pdf") and os.path.isfile(os.path.join(base_dir, f))
]

arquivos_gerados = []

for pdf_nome in arquivos_pdf:
    pdf_path = os.path.join(base_dir, pdf_nome)
    pdf = fitz.open(pdf_path)

    if len(pdf) > 1:
        for pagina_num in range(len(pdf)):
            novo_pdf = fitz.open()
            novo_pdf.insert_pdf(pdf, from_page=pagina_num, to_page=pagina_num)
            caminho_pagina = os.path.join(
                output_dir_paginas, f"{Path(pdf_nome).stem}_pagina_{pagina_num + 1}.pdf")
            novo_pdf.save(caminho_pagina)
            novo_pdf.close()
            arquivos_gerados.append(caminho_pagina)
    else:
        arquivos_gerados.append(pdf_path)

    pdf.close()

log("Processamento dos PDFs concluido.")

# 🔍 Extrair CNPJs dos arquivos em 'papelada'
pasta_papelada = os.path.join(base_dir, "papelada")
if os.path.exists(pasta_papelada):
    log("🔍 Buscando CNPJs nos arquivos de 'papelada'...")
    extrair_cnpjs_de_pdfs(pasta_papelada)
else:
    log("Pasta 'papelada' nao encontrada.")

# Enviar os e-mails
total_emails = len(arquivos_gerados)
for idx, arquivo in enumerate(arquivos_gerados, 1):
    log(f"Enviando ({idx}/{total_emails})...")
    enviar_email(arquivo)

log("Todos os e-mails foram enviados com sucesso!")

# 🔴 Limpar a pasta 'paginas_separadas' apos envio
try:
    for arquivo in os.listdir(output_dir_paginas):
        arquivo_path = os.path.join(output_dir_paginas, arquivo)
        if os.path.isfile(arquivo_path):
            os.remove(arquivo_path)
    log(f"Pasta '{output_dir_paginas}' limpa com sucesso.")
except Exception as e:
    log(f"Erro ao limpar a pasta de paginas separadas: {e}")

# 🔴 Excluir arquivos e pastas dentro de 'jrenova', exceto pastas preservadas
pastas_preservadas = {"sindificios", "fgts", "empresta", "papelada"}
try:
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path) and item not in pastas_preservadas:
            shutil.rmtree(item_path)
    log("Arquivos e pastas removidos, exceto as pastas preservadas.")
except Exception as e:
    log(f"Erro ao limpar a pasta '{base_dir}': {e}")
