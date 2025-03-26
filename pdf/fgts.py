import fitz
import os
import re
import smtplib
import mimetypes
from email.message import EmailMessage

# Configuração do e-mail
EMAIL_REMETENTE = "python@jaime.com.br"
EMAIL_LOGIN = "AKIAVA6I6DDDZ45THKCW"
EMAIL_SENHA = "BFaQl08bmO+QxeJzE8qTnR02ETo+3BhVAAwM5hgy3wYa"
EMAIL_DESTINATARIO = "alan.silva@jaime.com.br"  # Pode ser dinâmico se necessário
# Servidor SMTP do seu provedor
SMTP_SERVIDOR = "email-smtp.us-east-1.amazonaws.com"
SMTP_PORTA = 587  # Porta do SMTP

# Diretório de saída
output_dir_paginas = 'paginas_separadas'

# Limpar a pasta paginas_separadas antes de cada execução
if os.path.exists(output_dir_paginas):
    for arquivo in os.listdir(output_dir_paginas):
        caminho_arquivo = os.path.join(output_dir_paginas, arquivo)
        if os.path.isfile(caminho_arquivo):
            os.remove(caminho_arquivo)
    print("Pasta 'paginas_separadas' limpa!")
os.makedirs(output_dir_paginas, exist_ok=True)

# Função para extrair apenas o CNPJ (sem a palavra "CNPJ")


def extrair_cnpjs(texto):
    matches = re.findall(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', texto)
    return matches if matches else ["CNPJ não encontrado"]


# Abrir o PDF original
pdf = fitz.open("encargos_test.pdf")

# Lista para armazenar os arquivos gerados
arquivos_gerados = []

# Separar páginas e extrair CNPJ diretamente do texto
for pagina_num in range(len(pdf)):
    pagina = pdf.load_page(pagina_num)
    texto = pagina.get_text()
    cnpjs = extrair_cnpjs(texto)

    novo_pdf = fitz.open()
    novo_pdf.insert_pdf(pdf, from_page=pagina_num, to_page=pagina_num)
    caminho_pagina = os.path.join(
        output_dir_paginas, f"pagina_{pagina_num}.pdf")
    novo_pdf.save(caminho_pagina)
    novo_pdf.close()

    arquivos_gerados.append(caminho_pagina)
    print(f"Página {pagina_num}: " + " | ".join(cnpjs) + "\n")


pdf.close()
print("Páginas separadas e CNPJs extraídos com sucesso!")

# Função para enviar e-mails com anexo


def enviar_email(arquivo):
    msg = EmailMessage()
    msg['Subject'] = "Documento Gerado"
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = EMAIL_DESTINATARIO
    msg.set_content(
        f"Olá, segue o arquivo {os.path.basename(arquivo)} em anexo.")

    # Determinar o tipo MIME
    mime_tipo, _ = mimetypes.guess_type(arquivo)
    if mime_tipo is None:
        mime_tipo = "application/octet-stream"
    tipo_principal, tipo_sub = mime_tipo.split("/")

    # Anexar arquivo ao e-mail
    with open(arquivo, "rb") as f:
        msg.add_attachment(f.read(), maintype=tipo_principal,
                           subtype=tipo_sub, filename=os.path.basename(arquivo))

    # Enviar o e-mail
    with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as server:
        server.starttls()
        server.login(EMAIL_LOGIN, EMAIL_SENHA)
        server.send_message(msg)

    print(
        f"E-mail enviado com sucesso para {EMAIL_DESTINATARIO} com o arquivo {arquivo}")


# Enviar um e-mail para cada arquivo gerado
# for arquivo in arquivos_gerados:
#    enviar_email(arquivo)

# print("Todos os e-mails foram enviados com sucesso!")
