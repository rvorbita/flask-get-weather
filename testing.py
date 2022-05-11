import requests
from pprint import pprint


def check_city(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4b51614f99fbc6b7a79bd99ddcff9867&units=metric"

    r = requests.get(url).json()


    # try:
    #     if r:
    #         print(r['name'])

    # except KeyError:

    #     print(r['message'])

    return r



ask = input("enter city: ")


city = check_city(ask)



# pprint(city)
pprint(city)