from crypt import methods
from flask_app import app
from flask_app import api
import requests

from flask import render_template, request, session


@app.route('/')
def mainPage():

    return render_template('index.html')


@app.route('/newyork')
def newyorkPage():
    a_key = api.api_key

    city = "New York"
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={a_key}")

    result = response.json()

    data = {

        'status': result['weather'][0]['main'],
        'temp': round(result['main']['temp'], 1),
        'max_temp': round(result['main']['temp_max'], 1),
        'feels_like': round(result['main']['feels_like'], 1),
        'wind': round(result['wind']['speed'], 1)
    }

    return render_template('weather.html', data=data)


@app.route('/houston')
def houstonPage():
    a_key = api.api_key

    city = "houston"
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={a_key}")

    result = response.json()

    data = {

        'status': result['weather'][0]['main'],
        'temp': round(result['main']['temp'], 1),
        'max_temp': round(result['main']['temp_max'], 1),
        'feels_like': round(result['main']['feels_like'], 1),
        'wind': round(result['wind']['speed'], 1)
    }

    return render_template('weather.html', data=data)


@app.route('/miami')
def miamiPage():
    a_key = api.api_key

    city = "miami"
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={a_key}")

    result = response.json()

    data = {

        'status': result['weather'][0]['main'],
        'temp': round(result['main']['temp'], 1),
        'max_temp': round(result['main']['temp_max'], 1),
        'feels_like': round(result['main']['feels_like'], 1),
        'wind': round(result['wind']['speed'], 1)
    }

    return render_template('weather.html', data=data)


@app.route('/weatherPage', methods=['POST'])
def weatherPage():
    a_key = api.api_key

    city = request.form['city']
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={a_key}")

    result = response.json()

    print(result)

    data = {

        'status': result['weather'][0]['main'],
        'temp': round(result['main']['temp'], 1),
        'max_temp': round(result['main']['temp_max'], 1),
        'feels_like': round(result['main']['feels_like'], 1),
        'wind': round(result['wind']['speed'], 1)
    }
    return render_template('weather.html', data=data)
