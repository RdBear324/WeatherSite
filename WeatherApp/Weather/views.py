from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

API_KEY = 'f4515324282ff1f3b719932ba1abe1e6'


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()
    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }
    return render(request, 'weather/index.html', context)
