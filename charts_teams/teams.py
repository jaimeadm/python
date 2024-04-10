import pymsteams

WEBHOOK_NAME = "msteams-webhook"
WEBHOOK_URL = "teams_hook_here"

myTeamsMessage = pymsteams.connectorcard(WEBHOOK_URL)
myTeamsMessage.text("Enviar mensagem para um canal no Teams do Python")
myTeamsMessage.send()
