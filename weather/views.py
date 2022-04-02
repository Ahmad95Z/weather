import requests
from django.shortcuts import render
from .models import City

def index(request):
    appid = '32ac17f2b95b8028ea234304eae19886'
    url = 'https://api.openweathermap.org/data/2.5/weather?={}&units=metric&appid=' + appid

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city':city.name,
            'temp':res['main']['temp'],
            'icon':res['weather'][0]['icon']
        }
        all_cities.append(city_info)
    context = {'all_cities':all_cities}
    
    
    return render (request,'index.html',context)
    