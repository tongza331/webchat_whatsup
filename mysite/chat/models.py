from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=255,null=True, blank=True)
    password_room = models.CharField(max_length=255,null=True, blank=True)
    class Meta:
        db_table = 'room'

# class Message(models.Model):
#     username = models.CharField(max_length=255)
#     room = models.CharField(max_length=255)
#     content = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('date_added',)