import json, requests, shutil

#Get your key at https://api.nasa.gov/#apply-for-an-api-key

creds = {}
with open("creds.json", "r") as fi:
    creds = json.load(fi)

#Make a HTTP GET request to the NASA Astrology Picture of the Day API
req = requests.get("https://api.nasa.gov/planetary/apod?hd=true&api_key=9tTkSRNhJTVjWvNttmqPFyqxo9DpaAZi5mTW8hMK")
#Print out the HTTP request body
print(1, req.text)

#Load the HTTP request body into a JSON object
obj = json.loads(req.text)
#Get the URL for the picture with the 'url' key
pic_url = obj["url"]
#Print out the URL for the Picture of the Day
print(2, req.text)

#Make another HTTP GET request for the Picture of the Day, set the request streaming 
#option as True so that the whole request isn't fed into memory
pic_req = requests.get(pic_url, stream=True)
#Make sure that the HTTP request was successful before we try to save the picture by 
#checking that we got a 200 status code on the request response which represents a successful request
if pic_req.status_code == 200:
    #Open the target file in write bytes (wb) mode
    with open("nasa_apod.jpg", 'wb') as f:
        #Iterate over the raw response data and write it to the target file
        for chunk in pic_req.raw: #Alternatively, just using pic_req here works the same
            f.write(chunk)

#https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY