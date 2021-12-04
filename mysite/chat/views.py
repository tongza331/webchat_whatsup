from django.contrib import auth
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def homepage(request):
    return render(request,"chat/homepage.html")

def addRegister(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password_1=request.POST.get('password_1')
    password_2=request.POST.get('password_2')

    ## validate if password is equal
    if User.objects.filter(username=username).exists():
        messages.error(request, "This username has already been taken!")
        return redirect('homepage')
    else:
        if password_1==password_2:
            userCreate=User.objects.create_user(
                username=username,
                email=email,
                password=password_1,
            )
            userCreate.save()
            print("user created")
            return redirect('homepage')
        else:
            messages.error(request, "Password and Confirm password is not match.")
            return redirect('homepage')

def login_request(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			django_login(request,user)
			return redirect('room_list')
		else:
			if not User.objects.filter(username=username).exists():
				messages.error(request, "Username Doesn't Exist")
				return render(request,'chat/homepage.html',{'message3':"Username Doesn't Exist."})
				
			else:
				messages.info(request, "Incorrect Password")
				return render(request,'chat/homepage.html',{'message4':"Incorrect Password."})
	else:
		return render(request,'homepage.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

@login_required
def enter_room(request):
    ## Enter new room with password
    if request.method == "POST":
        username = request.user
        roomname = request.POST.get('roomname')
        passwordroom = request.POST.get('passwardroom')
        print(roomname,passwordroom)
        ## Validate room name and password room is correct.
        return redirect("room",username=username,room_name=roomname)

    ## if user enter new room who not create by yourself.
    return render(request,"chat/enter_room.html")

def create_new_room(request):
    ## if user create new room.
    if request.method=="POST":
        username = request.user
        room_name = request.POST.get('room_name')
        password_room = request.POST.get('passward_room')
        print(username,room_name,password_room)

        ## check this room name is exist.
        if RoomCreate.objects.filter(room_name=room_name).exists():
            print("This room name already exist.")
            messages.error(request, "This room name already exist.")
            return redirect("create_new_room")
        ## check this room name is not exist.
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
    print(username,'in room')
    msg = Message.objects.filter(roomname_msg=room_name)[0:25]

    ## check this room name is not exists
    if not RoomCreate.objects.filter(room_name=room_name).exists():
        messages.error(request, "This room name does not exist.")
        return redirect("enter_room")     
    else:
        get_username = User.objects.get(username=username)
        new_room = RoomCreate.objects.get(room_name=room_name)
        ## if user never enter this room. it will save to RoomList models
        try:         
            userJoin = RoomList.objects.get(username_id=get_username.id)
            if not userJoin.room_joined.filter(room_name=room_name).exists():
                userJoin.room_joined.add(new_room)
        except RoomList.DoesNotExist:
            ## Create this username in RoomList Models after that will save in M:M field
            addList = RoomList.objects.create(username_id=get_username.id)
            addList.room_joined.add(new_room)
            addList.save()
            return render(request, 'chat/room.html', {
            'room_name': room_name,
            'username':username,
            'msg':msg
        })
        return render(request, 'chat/room.html', {
                'room_name': room_name,
                'username':username,
                'msg':msg
            })
        

def room_list(request):
    ## show all room that user create.
    username = request.user
    print(username)
    roomlistCreate = RoomCreate.objects.filter(creater=username)
    try: 
        roomlistall = RoomList.objects.get(username_id=username.id)
        roomlistJoined = roomlistall.room_joined.all()

    except RoomList.DoesNotExist:
        roomlistJoined = None
    
    return render(request,"chat/your_room.html",{'roomlistCreate':roomlistCreate,
        'roomlistJoined':roomlistJoined
    })
