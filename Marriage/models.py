from django.db import models

# https://docs.djangoproject.com/en/5.0/topics/db/models/

class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=30)

class Guest(models.Model):
    name = models.CharField(max_length=30)
    side = models.CharField(max_length=30)