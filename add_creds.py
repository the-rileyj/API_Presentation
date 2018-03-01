import os, json

creds = {}

if os.path.exists("creds.json"):
    with open("creds.json", "r") as fi:
        creds = json.load(fi)

while True:
    key = input("Enter key for value: ")
    value = input("Enter key for value: ")
    if all(x.lower() not in ["cancel", "retry", "quit"] for x in [key, value]):
        creds[key] = value
        with open("creds.json", "w") as fi:
            json.dump(creds, fi)
    elif any(x.lower() == "quit" for x in [key, value]):
        break