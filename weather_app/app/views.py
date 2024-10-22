from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
from .models import City

def get_weather(request):
    if request.method == 'GET':
        city = request.GET.get('city', '')
        if city:
            # Check if the city is already in the database
            city_obj, created = City.objects.get_or_create(name=city)
            
            # API call to OpenWeatherMap
            api_key = '320e4e6b03a922598bd01e101a1a147a'  # Replace with your actual API key
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
                return JsonResponse(weather_data)
            else:
                return JsonResponse({'error': 'City not found'}, status=404)
        else:
            return JsonResponse({'error': 'Please provide a city name'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def weather_view(request):
    return render(request, 'weather.html')
