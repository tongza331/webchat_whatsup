from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class RoomCreate(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name="CreateRoom", blank=True, null=True)
    room_name = models.CharField(max_length=255,null=True, blank=True)
    password_room = models.CharField(max_length=255,null=True, blank=True)
    class Meta:
        db_table = 'room create'
    def __str__(self):
        return f"{self.creater},{self.room_name}"

class RoomList(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="EnteredRoom", blank=True, null=True)
    room_joined = ManyToManyField(RoomCreate, related_name="Joined_Other_Rooms", blank=True)
    class Meta:
        db_table = 'room list'
    def __str__(self):
        return f"{self.username}"

class Message(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Send_message", blank=True, null=True)
    roomname_msg = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'message history'
        ordering = ('date_added',)
    def __str__(self):
        return f"{self.username},{self.roomname_msg}"