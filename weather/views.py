from django.shortcuts import render
import json
import urllib.request
from urllib.parse import quote
from urllib import error


def WeatherApp(request):
    try:
        data = {}
        if request.method == 'POST':
            city = request.POST.get("city")
            encoded_city = quote(city)
            API_KEY = "974317af03374186e5b8f2c1660e606e"
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + encoded_city +
                                            '&units=metric&appid=' + API_KEY).read()
            ListData = json.loads(source)
            data = {
                'country_code': str(ListData['sys']['country']),
                'cor': str(ListData["coord"]["lon"]) + " " + str(ListData["coord"]["lat"]),
                'temp': str(ListData["main"]['temp']),
                'pressure': str(ListData['main']["pressure"]),
                'humidity': str(ListData['main']['humidity']),
                'main': str(ListData["weather"][0]['main']),
                'visibility': str(ListData["visibility"]),
                'wind': str(ListData["wind"]["speed"]),
                'icon': str(ListData['weather'][0]['icon']),
                'city': encoded_city
            }
            return render(request, "home_weather.html", data)
        return render(request, "home_weather.html", data)
    except error.HTTPError:
        error_context = "Please introduce valid data, because the city was not found!!!"
        return render(request, "home_weather_error.html", {"error_context": error_context})
