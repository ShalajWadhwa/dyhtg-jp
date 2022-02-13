from backend import news_api_func as news
from backend import coords_api_func as coords
from backend import weather_api as weather

import datetime
import json

#pip install newsapi-python 

# today = datetime.date.today() #add to file where refresh is called

def weather_warn():
    #read in data file
    with open('database/db.json', 'r') as openfile:
        data = json.load(openfile)
    warning_dict = {}
    num = 1
    warning_words = ["snow", "rain", "fog", "hail", "clouds"]
    for employee in data:
        lat = data[employee]['lat']
        long = data[employee]['long']
        descrBits = weather.get_weather(lat, long)[3].split()
    #print(descrBits)    
        for warning in warning_words:
            if warning in descrBits:
                lst = []
                first_name = data[employee]['first_name']
                last_name = data[employee]['last_name']
                region = data[employee]['city']
                lst.append(first_name)
                lst.append(last_name)
                lst.append(region)
                lst.append(warning)
                warning_dict[num] = lst
                num += 1
    with open('database/weather_warnings.json', 'w') as openfile:
        json.dump(warning_dict, openfile)


# def weather_news():
#     #read in data file
#     with open('database/db.json', 'r') as openfile:
#         data = json.load(openfile)

# def weather_graph():
#     #read in data file
#     with open('database/db.json', 'r') as openfile:
#         data = json.load(openfile)

#     for employee in data:
#         temp = data[employee]['weather'][0]

weather_warn()