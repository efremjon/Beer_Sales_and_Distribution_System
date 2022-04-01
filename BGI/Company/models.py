from django.db import models
#models should not be Distributed accross multiple app's models.py unless for app usability packaging purpose
# Create your models here.
class Profile(models.Model):
    img=models.ImageField()
    



class Product(models.Model):
    beer_name=models.CharField(max_length=20)
    price=models.FloatField()
    
class Store(models.Model):
    name=models.CharField(max_length=50)
    castel=models.IntegerField()
    senq=models.IntegerField()
    doppel=models.IntegerField()
    george=models.IntegerField()
    
    

class Store_manager(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=50)
    store=models.OneToOneField("Store",on_delete=models.CASCADE)
    profile=models.OneToOneField('Profile',on_delete=models.CASCADE)

class Finance(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=255)
    profile=models.OneToOneField('Profile',on_delete=None)

class Region(models.Model):
    pass

class Agent(models.Model):
    agent_name=models.CharField(max_length=50)
    agent_username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    region=models.ForeignKey("Region",on_delete=None)
    profile=models.OneToOneField('Profile',on_delete=None)

class Agent_store(models.Model):
    name=models.CharField(max_length=50)
    Agent=models.ForeignKey("Agent",on_delete=models.CASCADE)
    castel=models.IntegerField()
    senq=models.IntegerField()
    doppel=models.IntegerField()
    george=models.IntegerField()

class Driver(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=50)
    agent=models.ForeignKey("Agent",on_delete=models.CASCADE)
    profile=models.OneToOneField('Profile',on_delete=None)
    

class Agent_order(models.Model):
    transaction_code=models.CharField(max_length=255)
    agent=models.ForeignKey("Agent",on_delete=None)
    delivered=models.BooleanField(default=False)
    castel=models.IntegerField()
    senq=models.IntegerField()
    doppel=models.IntegerField()
    george=models.IntegerField()
    total_payment=models.FloatField()
    store=models.ForeignKey("Store",on_delete=None)

#customer's document should be  on their profile or
#find a way to store the relevant document of an agen and a customer 

class Customer(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=255)
    agent=models.ForeignKey("Agent",on_delete=models.CASCADE)
    profile=models.OneToOneField('Profile',on_delete=None)


class Customer_order(models.Model):
    transaction_code=models.CharField(max_length=255)
    customer=models.ForeignKey("Agent",on_delete=None)
    delivered=models.BooleanField(default=False)
    castel=models.IntegerField()
    senq=models.IntegerField()
    doppel=models.IntegerField()
    george=models.IntegerField()
    total_payment=models.FloatField()
    store=models.ForeignKey("Agent_store",on_delete=None)

class Agent_store_manager(models.Model):
        username=models.CharField(max_length=50)
        password=models.CharField(max_length=255)
        email=models.CharField(max_length=50)
        store=models.OneToOneField("Agent_store",on_delete=models.CASCADE)
        profile=models.OneToOneField('Profile',on_delete=models.CASCADE)
    
class Agent_finance(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    agent=models.ForeignKey("Agent",models.CASCADE)
    profile=models.OneToOneField('Profile',on_delete=None)








    

