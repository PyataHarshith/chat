from django.db import models
from datetime import datetime
# Create your models here.

class room(models.Model):
    name = models.CharField(max_length=1000)

class message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
