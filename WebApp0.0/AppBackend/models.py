from django.db import models

# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class Profile(models.Model):
    name = models.CharField(max_length = 50)
    address1 = models.CharField(max_length = 100)
    address2 = models.CharField(max_length = 100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 9)