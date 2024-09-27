from django.shortcuts import render
from showforecast.weatherparser import get_forecast_weather

# Create your views here.
def weather_shower(request):
    city=request.GET.get('city')
    data={
        'weather_data':get_forecast_weather(city),
        'city':city,
    }
    print(data['city'])
    return render(request,'showforecast/forecastshower.html',context=data)