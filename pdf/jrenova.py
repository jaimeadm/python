#!/usr/bin/python3
"""
Script: jrenova.py
Atualizado em: 27/03/2025
Autor: Alan M O Silva
Descrição: Lê todos os PDFs na pasta "/mnt/jrenova", separa páginas (se necessário) e envia por e-mail.
"""
__version__ = "1.0.0"

import fitz
import os
import smtplib
import mimetypes
import time
import shutil
from pathlib import Path
from email.message import EmailMessage

# Configuração do e-mail
EMAIL_REMETENTE = "jrenova@jaime.com.br"
EMAIL_LOGIN = "AKIAVA6I6DDD76RKVPJV"
EMAIL_SENHA = "BJvvlO7tblcWijPfxiANMi5FKvscEHWqZhlBlCB7rhJy"
EMAIL_DESTINATARIO = "alan.silva@jaime.com.br"
SMTP_SERVIDOR = "email-smtp.sa-east-1.amazonaws.com"
SMTP_PORTA = 587

# Diretórios
base_dir = "/mnt/jrenova"
output_dir_paginas = os.path.join(base_dir, "paginas_separadas")
os.makedirs(output_dir_paginas, exist_ok=True)


def enviar_email(arquivo):
    msg = EmailMessage()
    msg['Subject'] = "Documento Gerado"
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINATARIO
    msg.set_content(
        f"Olá, segue o arquivo {os.path.basename(arquivo)} em anexo.")

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

    print(f"E-mail enviado para {EMAIL_DESTINATARIO} com o arquivo {arquivo}")
    time.sleep(5)  # Pausa de 5 segundos após cada envio


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

print("Processamento dos PDFs concluído.")

# Enviar os e-mails
for arquivo in arquivos_gerados:
    enviar_email(arquivo)

print("Todos os e-mails foram enviados com sucesso!")

# 🔴 Limpar a pasta 'paginas_separadas' após envio
try:
    for arquivo in os.listdir(output_dir_paginas):
        arquivo_path = os.path.join(output_dir_paginas, arquivo)
        if os.path.isfile(arquivo_path):
            os.remove(arquivo_path)
    print(f"Pasta '{output_dir_paginas}' limpa com sucesso.")
except Exception as e:
    print(f"Erro ao limpar a pasta de páginas separadas: {e}")

# 🔴 Excluir todos os arquivos e pastas dentro da pasta 'jrenova'
try:
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    print(
        f"Todos os arquivos e pastas dentro de '{base_dir}' foram removidos com sucesso.")
except Exception as e:
    print(f"Erro ao limpar a pasta '{base_dir}': {e}")
