import pymsteams

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard("https://jaimeo365.webhook.office.com/webhookb2/60cbe599-1ce3-4a29-b8e3-58622244d7a4@10e10d15-d448-4805-a5bf-546d766ddffa/IncomingWebhook/8c762f7266ad4a52a2220779a91f7506/7a3b0c00-9c1b-41ce-b8e2-0167bf73baf4")

# Add text to the message.
myTeamsMessage.color("#349eeb")
myTeamsMessage.title("This is my message title")
myTeamsMessage.text("this is my text")

# create the section
myMessageSection = pymsteams.cardsection()

# Section Title
myMessageSection.title("Section title")

# Activity Elements
myMessageSection.activityTitle("my activity title")
myMessageSection.activitySubtitle("my activity subtitle")
myMessageSection.activityImage("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDg7WNkAi4jSfWl-CA4aLMxJAOBxBGVNXe1gwSWFnR5Q&s")
myMessageSection.activityText("This is my activity Text")

# Facts are key value pairs displayed in a list.
myMessageSection.addFact("this", "is fine")
myMessageSection.addFact("this is", "also fine")

# Section Text
myMessageSection.text("This is my section text")

# Section Images
myMessageSection.addImage("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDg7WNkAi4jSfWl-CA4aLMxJAOBxBGVNXe1gwSWFnR5Q&s", ititle="This Is Fine")

# Add your section to the connector card object before sending
myTeamsMessage.addSection(myMessageSection)

# Then send the card
myTeamsMessage.send()
