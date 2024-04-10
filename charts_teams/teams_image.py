import pymsteams

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard("https://jaimeo365.webhook.office.com/webhookb2/60cbe599-1ce3-4a29-b8e3-58622244d7a4@10e10d15-d448-4805-a5bf-546d766ddffa/IncomingWebhook/8c762f7266ad4a52a2220779a91f7506/7a3b0c00-9c1b-41ce-b8e2-0167bf73baf4")

# Add text to the message.
myTeamsMessage.color("#349eeb")
myTeamsMessage.title("Relatório de Telefonia")
myTeamsMessage.addLinkButton("Clique aqui para visualizar", "https://cdn-icons-png.flaticon.com/512/404/404621.png")
myTeamsMessage.text("Relatório com o total de ligações da última semana e o total de problemas que nos foi reportado.")

# create the section
myMessageSection = pymsteams.cardsection()

# Section Title
#myMessageSection.title("Gráfico")

# Section Images
myMessageSection.addImage("https://cdn-icons-png.flaticon.com/512/404/404621.png", ititle="Gráfico")

# Add your section to the connector card object before sending
myTeamsMessage.addSection(myMessageSection)

# Then send the card
myTeamsMessage.send()