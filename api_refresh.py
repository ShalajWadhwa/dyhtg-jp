from backend import news_api_func as news
from backend import coords_api_func as coords
from backend import weather_api as weather
from dashboard import weather_graph, weather_warn

import datetime
import json

#pip install newsapi-python 

# today = datetime.date.today() #add to file where refresh is called

def refresh(today, news_api_key, weather_api_key):
    # read in data file
    with open('database/db.json', 'r') as openfile:
        data = json.load(openfile)

    for employee in data:
        region = data[employee]['city']
        lat = data[employee]['lat']
        long = data[employee]['long']
        weat_news = ()
        weat_news += (weather.get_weather(lat, long, weather_api_key),)
        weat_news += (news.get_news(region, today, news_api_key),)
        data[employee]['weather'] = weat_news[0]
        data[employee]['news'] = weat_news[1]

    #rewrite data file with added info
    with open('database/db.json', 'w') as openfile:
        json.dump(data, openfile)
    
    weather_graph(data)

    weather_warn(data)
