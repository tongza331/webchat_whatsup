from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('register', views.addRegister, name='addRegister'),
    path('login/', views.login_request, name='login_request'),
    path('EnterRoom',views.enter_room,name='enter_room'),
    path('chatroom/<str:room_name>/<str:username>/', views.room, name='room'),   
    path('myRoom',views.room_list,name='room_list'),
    path('CreateNewRoom',views.create_new_room,name="create_new_room"),
    path('logout/',views.logout,name='logout'),
]
