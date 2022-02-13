from backend import news_api_func as news
from backend import coords_api_func as coords
from backend import weather_api as weather

import datetime
import json
import matplotlib.pyplot as plt

#pip install newsapi-python 
#pip install matplotlib

#today = datetime.date.today() #add to file where refresh is called

def weather_warn():
    #read in data file
    with open('database/db.json', 'r') as openfile:
        data = json.load(openfile)
    warning_dict = {}
    num = 1
    warning_words = ["snow", "rain", "fog", "hail"]
    for employee in data:
        lat = data[employee]['lat']
        long = data[employee]['long']
        descrBits = data[employee]['weather'][3].split()
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

def weather_graph():
    #read in data file
    with open('database/db.json', 'r') as openfile:
        data = json.load(openfile)

    city_list = []
    temp_list = []
    for employee in data:
        region = data[employee]['city']
        if region not in city_list:
            city_list.append(region)
            temp = int(data[employee]['weather'][0])
            temp_list.append(temp)
    plt.bar(city_list, temp_list)
    plt.xlabel("Cities")
    plt.ylabel("Temperature")
    plt.savefig('database/temp_cities.png')