from django.db import models
#models should not be Distributed accross multiple app's models.py unless for app usability packaging purpose
# Create your models here.
class Profile(models.Model):
    img=models.ImageField()
    Company_Name=models.CharField(max_length=200)
class Product(models.Model):
    beer_name=models.CharField(max_length=20)
    price=models.FloatField(default=0.0)
    
class Store(models.Model):
    name=models.CharField(max_length=50)
    castel=models.IntegerField(default=10,help_text="The minimal amount 10")
    senq=models.IntegerField(default=10,help_text="The minimal amount 10")
    doppel=models.IntegerField(default=10,help_text="The minimal amount 10")
    george=models.IntegerField(default=10,help_text="The minimal amount 10")
    
    

class Store_manager(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=50)
    #store=models.OneToOneField("Store",on_delete=models.CASCADE)
    #profile=models.OneToOneField('Profile',on_delete=models.CASCADE)

class Finance(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=255)
    #profile=models.OneToOneField('Profile',on_delete=None)

class Region(models.Model):
    region_name=models.CharField(max_length=300)
