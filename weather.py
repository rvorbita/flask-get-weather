from app import app




#using weather api
# from itertools import count
# import requests
# from pprint import pprint

# API_KEY="4b51614f99fbc6b7a79bd99ddcff9867"

# city=input("Enter City Name: ")

# base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
# weather_data = requests.get(base_url).json()

# city = weather_data['name']
# country = weather_data['sys']['country']
# weather = weather_data['weather']
# weather_main = weather_data['weather'][0]['main']
# weather_desc = weather_data['weather'][0]['description']
# # weather_main = [ i['main'] for i in weather ]
# # weather_desc = [ i['description'] for i in weather ]

# pprint(weather_data)
# print(city + ',' + country)
# print(f"Main: {weather_main}")
# print(f"Description: {weather_desc}")