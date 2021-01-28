from django.db import models

# Create your models here.


class Carshop(models.Model):
    first = models.CharField(max_length=25,blank=True)
    last = models.CharField(max_length=25,blank=True)
    email=models.EmailField(max_length=40,blank=True)
    address = models.CharField(max_length=55,blank=True)
    #number  = models.CharField(max_length=25,blank=True)
    #date = models.DateField(max_length=25,blank=True)
    #time = models.TimeField(max_length=25,blank=True)
    def __str__(self):
        return self.first


class Shash(models.Model):
    first = models.CharField(max_length=25,blank=True)
    last = models.CharField(max_length=25,blank=True)
    email=models.EmailField(max_length=40,blank=True)
    address = models.CharField(max_length=55,blank=True)
    number = models.CharField(max_length=12,blank=True)
    date = models.DateField()
    
    def __str__(self):
        return self.first

