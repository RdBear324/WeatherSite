from django.shortcuts import render
import requests

API_KEY = 'f4515324282ff1f3b719932ba1abe1e6'


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY
    city = 'Minsk'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }
    context = {
        'info': city_info
    }
    return render(request, 'weather/index.html', context)
