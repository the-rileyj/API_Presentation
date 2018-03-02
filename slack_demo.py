from slackclient import SlackClient
from time import sleep
import json, requests

creds = {}
with open("creds.json", "r") as fi:
    creds = json.load(fi)
sc = SlackClient(creds["slack"])

resp_obj1 = sc.api_call(
  "chat.postMessage",
  channel="#programmingclub",
  text="CSS is my favorite programming language!",
  as_user=True
) 

response2 = requests.post("https://slack.com/api/chat.postMessage", data={"token": creds["slack"], "channel": "#programmingclub", "text": "CSS is my favorite programming language!", "as_user": "true"})
resp_obj2 = json.loads(response2.text)

sleep(5)

print(resp_obj1["ts"], resp_obj2["ts"])

sc.api_call(
  "chat.delete",
  channel=resp_obj1["channel"],
  ts=resp_obj1["ts"],
  as_user=True
)

response2 = requests.post("https://slack.com/api/chat.delete", data={"token": creds["slack"], "channel": resp_obj1["channel"], "ts": resp_obj2["ts"], "as_user": "true"})
