from django.db import models
from datetime import time

# Create your models here.
#make migration: python manage.py makemigrations
#show migration: python manage.py showmigrations
#to run migrate: python manage.py migrate

class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} room {self.room_number} on floor {self.floor}"

class Meeting(models.Model): #represnt table in db
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9)) #must have default
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
