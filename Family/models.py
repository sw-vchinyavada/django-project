from django.db import models

# https://docs.djangoproject.com/en/5.0/topics/db/models/

class Member(models.Model):
    name = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)