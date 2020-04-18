from django.db import models

# Create your models here.
class Meeting(models.Model): #represnt table in db
    title = models.CharField(max_length=200)
    date = models.DateField()