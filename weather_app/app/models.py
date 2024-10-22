from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"

class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='weather_data')
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city.name} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
