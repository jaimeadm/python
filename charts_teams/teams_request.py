import requests
import json


def post_message_to_teams():

    url_webhook = "teams_hook_here"
    # files = {'file': open('chart.png', 'rb')}

    headers = {
        'Content-Type': 'application/json'  # multipart/form-data
    }

    payload = {
        "text": "\n A tabela está atualizada,\n"
        "\n Mensagem,\n"
        "\n test \n"
    }

    response = requests.post(url_webhook, headers=headers,
                             data=json.dumps(payload))  # files=files


# Post Message to Teams
post_message_to_teams()
