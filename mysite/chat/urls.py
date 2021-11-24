from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('index',views.index,name='index'),
    path('register', views.addRegister, name='addRegister'),
    path('login', views.login_request, name='login_request'),
    path('EnterRoom',views.enter_room,name='enter_room'),
    path('chat/<str:room_name>/', views.room, name='room'),   
    path('/logout/',views.logout,name='logout'),
]

