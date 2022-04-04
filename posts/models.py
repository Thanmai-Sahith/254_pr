from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
class user(models.Model):
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    
