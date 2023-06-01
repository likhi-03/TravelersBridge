from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.FloatField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_booked = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return f"{self.hotel} - Room {self.room_number}"


class Hotel_Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Hotel_bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='Hotel_bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.room} ({self.check_in} to {self.check_out})"