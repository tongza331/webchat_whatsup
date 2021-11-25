from django.contrib import admin
from django.db.models.aggregates import Count
from chat.models import *
# Register your models here.
@admin.register(RoomCreate)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['creater','room_name']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['username','roomname_msg','date_added']

@admin.register(RoomList)
class RoomListAdmin(admin.ModelAdmin):
    list_display = ['username']
