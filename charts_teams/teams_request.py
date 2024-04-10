import requests
import json

def post_message_to_teams():

    url_webhook = "https://jaimeo365.webhook.office.com/webhookb2/60cbe599-1ce3-4a29-b8e3-58622244d7a4@10e10d15-d448-4805-a5bf-546d766ddffa/IncomingWebhook/8c762f7266ad4a52a2220779a91f7506/7a3b0c00-9c1b-41ce-b8e2-0167bf73baf4"
    #files = {'file': open('chart.png', 'rb')}

    headers = {
        'Content-Type': 'application/json' # multipart/form-data
    }

    payload = {
        "text": "\n A tabela está atualizada,\n"
        "\n Mensagem,\n"
        "\n test \n"
    }

    response = requests.post(url_webhook, headers=headers, data=json.dumps(payload)) # files=files

# Post Message to Teams
post_message_to_teams()
