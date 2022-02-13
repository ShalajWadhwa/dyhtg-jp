import requests

def get_weather(lat, lon):
        params = {"apiid" : "32bdf1ac7b5820c712199642efd9ee76",
                "units" : "metric"}

        url = "https://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid=32bdf1ac7b5820c712199642efd9ee76".format(lat, lon)

        response=requests.get(url,params)
        response = response.json()
        temp = (response['main']['temp'])
        feels_like = (response['main']['feels_like'])
        wind = (response['wind']['speed'])
        weather = (response['weather'][0]['description'])

        return temp, feels_like, wind, weather