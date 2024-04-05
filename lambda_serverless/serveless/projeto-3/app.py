import requests

# https://api.telegram.org/bot{{TOKEN}}/getUpdates

bot_token = '6457401113:AAEd-R15VRD3azLIzLpLzavsyB96JSxy8bY'
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
