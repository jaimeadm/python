import os
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv # type: ignore
from string import Template
import smtplib

load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'substituir.html'

# Remetente e destinatário
#remetente = os.getenv('FROM_EMAIL', '')
remetente = 'helpdesk@jaime.com.br'
destinatario = 'alan.silva@jaime.com.br'

# SMTP
smtp_server = 'email-smtp.us-east-1.amazonaws.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem
with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Fulano')

# Transformar mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Enviar e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso')