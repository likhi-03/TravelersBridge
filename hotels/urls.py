from django.urls import path
from . import views

urlpatterns = [
    path('hotel/',views.hotelsearch,name="hotelsearch"),
    path('hotel/<str:location>/', views.hotel_search, name='hotel_search'),
    path('hotel/<str:hotel_name>', views.hotel_details, name='hotel_details'),
    path('room/<int:room_id>', views.book_room, name='book_room'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
]
