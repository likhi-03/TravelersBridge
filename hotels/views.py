from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Hotel, Room, Hotel_Booking

from django.urls import reverse

def hotelsearch(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        return redirect(reverse('hotel_search', kwargs={'location': location}))

    return render(request, 'hotel.html')

def hotel_search(request, location):
    hotels = Hotel.objects.filter(location__icontains=location)
    return render(request, 'search_hotel.html', {'hotels': hotels})

def hotel_details(request, hotel_name):
    hotel = get_object_or_404(Hotel, name=hotel_name)
    return render(request, 'hotel_details.html', {'hotel': hotel})

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if room.is_booked:
        messages.error(request, 'This room is already booked.')
        return redirect('hotel')

    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        booking = Hotel_Booking(user=request.user, room=room, check_in=check_in, check_out=check_out, name=name, mobile=mobile)
        booking.save()
        room.is_booked = True
        room.save()
        messages.success(request, 'Room booked successfully.')
        return redirect('hotel')

    return render(request, 'hotel_booking.html', {'room': room})

@login_required
def my_bookings(request):
    Hotel_bookings = Hotel_Booking.objects.filter(user=request.user)
    return render(request, 'my_booking.html', {'Hotel_bookings': Hotel_bookings})
