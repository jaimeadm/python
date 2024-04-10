import requests

# https://api.telegram.org/bot{{TOKEN}}/getUpdates

bot_token = 'api_token_here'
id_canal = '-1002064525270'

api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'


def enviar_mensagem_telegram(mensagem):
    resposta = requests.post(
        api_url,
        json={
            "chat_id": id_canal,
            "text": mensagem
        }
    )
