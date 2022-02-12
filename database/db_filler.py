import json
import requests
import time

'''
"First Name", "Last Name", "Email", "Phone", "Post Code", "Weather", "News", "Internet Connection", "lat", "lng"
'''
URL = "https://random-data-api.com/api/users/random_user"

db = {}


for emp in range(5):
    response = requests.get(url = URL).json()
    db[response['id']] = {"first_name" : response["first_name"], "last_name" : response["last_name"], "email" : response["email"], "phone_number" : response["phone_number"], "post_code" : None, "weather" : None, "news" : None, "service" : None, "lat" : None, "long" : None}
    time.sleep(0.5)

with open("database/db.json", "w") as f:
    json.dump(db, f)