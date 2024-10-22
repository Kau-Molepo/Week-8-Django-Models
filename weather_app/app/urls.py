from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather_view, name='weather_view'),
    path('get_weather/', views.get_weather, name='get_weather'),
]

