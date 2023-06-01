
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TouristSpot(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
