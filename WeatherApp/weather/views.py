import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.


def index(request):
    appid = '1ba497ca876a6096ca8c74fb4ecdea7d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' +appid

    # city = 'London'

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    # to clear up the form for the next city
    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': int(res['main']['temp']),
            'humidity': res['main']['humidity'],
            'icon': res['weather'][0]['icon'],
            # 'sky': res['weather'][0]['main']
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)