from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('homepage',views.homepage,name='homepage'),
    path('<str:room_name>/', views.room, name='room'),   
]

