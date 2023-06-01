from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from math import ceil
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from .models import Contact
import json
# Create your views here.
def index(request):
	return render(request,'home.html')

def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('index')
        else:
            messages.warning(request, "Invalid credentials! Please try again")
            return redirect('index')
    return render(request,'login.html')
    
def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email1']
        phone = request.POST['phone']
        password = request.POST['password']
        password1 = request.POST['password1']

        # check for errorneous input
        if (password1 != password):
            messages.warning(request, " Passwords do not match")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        try:
            user = User.objects.get(username=username)
            messages.warning(request, " Username Already taken. Try with different Username.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except User.DoesNotExist:
            # Create the user
            myuser = User.objects.create_user(username=username, email=email, password=password)
            myuser.first_name = f_name
            myuser.last_name = l_name
            myuser.phone = phone
            myuser.save()
            messages.success(request, " Your Account has been successfully created")
            return redirect('index')
    else:
        return render(request,'signup.html')
def vacation(request):
    return render(request,'vacation.html')
def flight(request):
    return render(request,'flight.html')
def contact(request):
    return render(request,'contact.html')
def car(request):
    return render(request,'car.html')
def hotel(request):
    return render(request,'hotel.html')
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully. Thank you!')
        thank = True
        return render(request, 'home.html', {'thank': thank})
    return render(request, 'contact.html', {'thank': thank})


