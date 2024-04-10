import pymsteams

WEBHOOK_NAME = "msteams-webhook"
WEBHOOK_URL = "https://jaimeo365.webhook.office.com/webhookb2/60cbe599-1ce3-4a29-b8e3-58622244d7a4@10e10d15-d448-4805-a5bf-546d766ddffa/IncomingWebhook/8c762f7266ad4a52a2220779a91f7506/7a3b0c00-9c1b-41ce-b8e2-0167bf73baf4"

myTeamsMessage = pymsteams.connectorcard(WEBHOOK_URL)
myTeamsMessage.text("Enviar mensagem para um canal no Teams do Python")
myTeamsMessage.send()
