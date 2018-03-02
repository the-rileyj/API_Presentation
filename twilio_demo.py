from twilio.rest import Client
import json

creds = {}
with open("creds.json", "r") as fi:
    creds = json.load(fi)

client = Client(creds["twilio_sid"], creds["twilio_token"])

message = client.messages.create(
    to=creds["my_number"], 
    from_=creds["comp_number"],
    body="Hello !"
)