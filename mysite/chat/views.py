from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request,"chat/homepage.html")

def index(request):
    return render(request,"chat/index.html")


def addRegister(request):
    username=request.POST['username']
    email=request.POST['email']
    password_1=request.POST['password_1']
    password_2=request.POST['password_2']

    user=User.objects.create_user(
        username=username,
        email=email,
        password=password_1,
    )
    user.save()
    print("user created")
    return redirect('homepage')

def login_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        django_login(request,user)
        print("login sucessfull.")
        return redirect('enter_room')
    else:
        if not User.objects.create_user(username=username).exists():
            print("Username already exists.")
        else:
            print("Incorrect password.")
    return redirect('homepage')

def logout(request):
	auth.logout(request)
	return redirect('/')

@login_required
def enter_room(request):
    return render(request,"chat/enter_room.html")

def room(request, room_name):
    username = request.GET.get('username','Anonymous')
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username':username
    })