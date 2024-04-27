from django.db import models

# Create your models here.
class userregister(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

class sentiments(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100, default='Neutral')
    sentiment = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
