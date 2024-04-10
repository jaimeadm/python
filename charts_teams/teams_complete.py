import pymsteams

# You must create the connectorcard object with the Microsoft Webhook URL
myTeamsMessage = pymsteams.connectorcard("teams_hook_here")

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
myMessageSection.activityImage(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDg7WNkAi4jSfWl-CA4aLMxJAOBxBGVNXe1gwSWFnR5Q&s")
myMessageSection.activityText("This is my activity Text")

# Facts are key value pairs displayed in a list.
myMessageSection.addFact("this", "is fine")
myMessageSection.addFact("this is", "also fine")

# Section Text
myMessageSection.text("This is my section text")

# Section Images
myMessageSection.addImage(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDg7WNkAi4jSfWl-CA4aLMxJAOBxBGVNXe1gwSWFnR5Q&s", ititle="This Is Fine")

# Add your section to the connector card object before sending
myTeamsMessage.addSection(myMessageSection)

# Then send the card
myTeamsMessage.send()
