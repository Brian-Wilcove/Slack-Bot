import os
import csv
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

#Create a list from our csv
file = open("data.csv", "r")
data = list(csv.DictReader(file, delimiter=","))
file.close()

# Set the SLACK_BOT_TOKEN as an environment variable
# WebClient instantiates a client that can call API methods
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))

# Create a for loop of each value in our csv
for row in data:
    # Call the user_lookupByEmail method using the WebClient
    result = client.users_lookupByEmail(
        email = row["Email"]
    )
    User_ID=result.get("user").get("id")
    # Call the chat.postMessage method using the WebClient
    result = client.chat_postMessage(
        channel=User_ID, 
        # text="Hello world",
        text = row["Message"]
    )
