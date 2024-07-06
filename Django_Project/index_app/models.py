from django.db import models
from .models import *
from django.contrib.auth.models import User
from django.conf import settings

class NewArrival(models.Model):
    image = models.ImageField(upload_to='image')  
    class Meta:
        db_table='NewArrival'

class Brand(models.Model):
    image = models.ImageField(upload_to='Brand')  
    class Meta:
        db_table='Brand'

class Address(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    AddressLine1 = models.TextField()
    AddressLine2 = models.TextField()
    City = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    PinCode = models.IntegerField()
    mobile = models.CharField(max_length=20)
    class Meta:
        db_table = "Address"