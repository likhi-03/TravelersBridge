from django.urls import path
from . import views


urlpatterns = [
    path('vacation_search/', views.vacation_search, name='vacation_search'),
]
