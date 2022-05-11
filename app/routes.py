from flask import render_template, url_for, redirect, flash, request
from app import app,db
from app.forms import WeatherForm
import requests
from app.models import City
from sqlalchemy import asc, desc




API_KEY="4b51614f99fbc6b7a79bd99ddcff9867"


def check_city(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4b51614f99fbc6b7a79bd99ddcff9867&units=metric"

    r = requests.get(url).json()

    message = ""

    try:
        if r:
            message = r['name']

    except KeyError:
            message = r['message']

    return message


@app.route('/home/<int:page_num>', methods=['GET', 'POST'])
def home(page_num):


    form = WeatherForm()

    if form.validate_on_submit():
        new_city = form.city.data
        
        c = check_city(new_city)
        
        if c != 'city not found':
            new_city_obj = City(name=c)
            db.session.add(new_city_obj)
            db.session.commit()
            flash(f"Success you have Added new City Weather.")
        else:
            flash(f"{c}")

        return redirect(url_for('home', page_num=1))
                

    # cities = City.query.all()
     #set pagination configuration settings
    cities = City.query.order_by(City.created_at.desc()).paginate(per_page=3, page=page_num, error_out=True)
    # cities = City.query.paginate(per_page=3, page=page_num, error_out=True)
    #set page pagination configuration
    weather_data = []

    for city in cities.items:

        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city.name}&appid=4b51614f99fbc6b7a79bd99ddcff9867&units=metric"
        r = requests.get(base_url).json()
        

        weather = {
            'city': city.name,
            'country': r['sys']['country'],
            'weather': r['weather'],
            'temp': round(r['main']['temp']),
            'weather_main': r['weather'][0]['main'],
            'weather_desc': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(weather)


    return render_template('home.html', title='Home', form=form, weather_data=weather_data, cities=cities)





@app.route('/views')
def views():

    cities = City.query.order_by(City.created_at.desc()).all()

    cities_data = []

    for city in cities:

        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city.name}&appid=4b51614f99fbc6b7a79bd99ddcff9867&units=metric"
        r = requests.get(base_url).json()
        
        weather = {
            'city': city.name,
            'country': r['sys']['country'],
            'weather': r['weather'],
            'temp': round(r['main']['temp']),
            'weather_main': r['weather'][0]['main'],
            'weather_desc': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'created_at': city.created_at,
        }

        cities_data.append(weather)

    return render_template('views.html', cities_data=cities_data)





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