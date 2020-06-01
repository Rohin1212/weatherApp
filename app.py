import json
import urllib.request
from flask import Flask, render_template, request, redirect, url_for
from datetime import date

app = Flask(__name__)
def kelv_to_celc(temp):
    return round(temp - 273.15,1)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/display', methods = ['POST'])  
def display(): 
    if request.method == 'POST':
        city = request.form['city']
        country = request.form['country']
        final_weather_data = {}
        try:
            weather_api = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=8b1f554d266a4addbfb19f2905f74e17"
            with urllib.request.urlopen(weather_api) as weather_url:
                weather_data = json.loads(weather_url.read().decode())
                final_weather_data['city'] = city.title()
                final_weather_data['country'] = country.title()
                final_weather_data['temp'] = kelv_to_celc(weather_data['main']['temp'])
                final_weather_data['temp_min'] = kelv_to_celc(weather_data['main']['temp_min'])
                final_weather_data['temp_max'] = kelv_to_celc(weather_data['main']['temp_max'])
                final_weather_data['descp'] = weather_data['weather'][0]['main']
                final_weather_data['wind'] = weather_data['wind']['speed']
                final_weather_data['humidity'] = weather_data['main']['humidity']
                my_date = date.today()
                final_weather_data['day'] = my_date.strftime("%B %d %Y")
        except:
            error = 'Sorry, could not find it!'
            return render_template('index.html', error = error)

        return render_template('index.html', final_weather_data = final_weather_data)

if(__name__ == '__main__'):
    app.run(debug = True)

#8b1f554d266a4addbfb19f2905f74e17
#https://api.openweathermap.org/data/2.5/weather?q=Melbourne,aus&appid=8b1f554d266a4addbfb19f2905f74e17



#a71be890-9957-11ea-be66-c93168939237

          #with urllib.request.urlopen("https://geolocation-db.com/json/fe80::7535:35db:43aa:339b%19") as url:
           #     data = json.loads(url.read().decode())
            #    latitude = data['latitude']
             #   longitude = data['longitude']