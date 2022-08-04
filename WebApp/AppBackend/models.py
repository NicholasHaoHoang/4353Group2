from django.db import models

# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class Profile(models.Model):
    id = models.AutoField(primary_key=True, editable = True)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length=100,blank = True)
    address1 = models.CharField(max_length = 100)
    address2 = models.CharField(max_length = 100, blank=True, default='')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length = 2)
    zipcode = models.CharField(max_length = 9)
# class UserDetails(models.Model):
#     email = models.CharField(primary_key=True,max_length=100,blank = True)
#     name = models.CharField(max_length=100)
#     ID = models.AutoField()

class FuelQuote(models.Model):
    email = models.CharField(max_length=100,blank = True)
    quoteId = models.AutoField(primary_key=True)
    gallonsRequested = models.IntegerField(default=0)
    deliveryAddress = models.CharField(max_length=100)
    deliverydate = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    AmountDue = models.IntegerField(default=0)



