from django.contrib import auth
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request,"chat/homepage.html")

def addRegister(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password_1=request.POST.get('password_1')
    password_2=request.POST.get('password_2')

    user=User.objects.create_user(
        username=username,
        email=email,
        password=password_1,
    )
    user.save()
    print("user created")
    return redirect('homepage')

def login_request(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        django_login(request,user)
        print("login sucessfull.")
        return redirect('room_list')
    else:
        if not User.objects.create_user(username=username).exists():
            print("Username Doesn't Exist.")
        else:
            print("Incorrect password.")
    return redirect('homepage')

def logout(request):
	auth.logout(request)
	return redirect('/')

@login_required
def enter_room(request):
    return render(request,"chat/enter_room.html")

def create_new_room(request):
    if request.method=="POST":
        username = request.user
        room_name = request.POST.get('room_name')
        password_room = request.POST.get('passward_room')
        roomall = RoomCreate.objects.all()
        print(username,room_name,password_room)
        for item in range(len(roomall)):
            if room_name == roomall[item].room_name:
                messages.error(request, "This room name already exist.")
                print("This room name already exist.")
                return redirect("create_new_room")
            else:
                RoomCreate.objects.create(
                    creater = username,
                    room_name = room_name,
                    password_room = password_room
                )
                print("Create new room success.")
                return redirect('room',room_name=room_name,username=username)
    return render(request,"chat/create_room.html")

def room(request, room_name,username):
    if request.method=="POST":
        roomall = RoomCreate.objects.all()
        for item in range(len(roomall)):
            if room_name != roomall[item].room_name:
                messages.error(request, "This room name does not exist.")
                return redirect("enter_room")
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username':username
    })

def room_list(request):
    username = request.user
    print(username)
    roomlistCreate = RoomCreate.objects.filter(creater=username)
    return render(request,"chat/your_room.html",{'roomlistCreate':roomlistCreate})
