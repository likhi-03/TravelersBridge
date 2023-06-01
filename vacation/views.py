from django.shortcuts import render, get_object_or_404
from .models import City

def vacation(request):
    cities = City.objects.all()
    return render(request, 'vacation.html', {'cities': cities})

def vacation_search(request):
    cities = City.objects.all()
    city_id = request.GET.get('city')
    city = get_object_or_404(City, id=city_id)
    spots = city.touristspot_set.all()
    return render(request, 'vacation_search.html', {'city': city, 'spots': spots, 'cities': cities})
