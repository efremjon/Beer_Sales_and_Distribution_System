from django.db import models

# Create your models here.
class Agent(models.Model):
    agent_name=models.CharField(max_length=50)
    agent_username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
   #region=models.ForeignKey("Region",on_delete=None)
    #profile=models.OneToOneField('Profile',on_delete=None)

class Agent_store(models.Model):
    name=models.CharField(max_length=50)
    #Agent=models.ForeignKey("Agent",on_delete=models.CASCADE)
    castel=models.IntegerField(default=0)
    senq=models.IntegerField(default=0)
    doppel=models.IntegerField(default=0)
    george=models.IntegerField(default=0)

class Driver(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=50)
    #agent=models.ForeignKey("Agent",on_delete=models.CASCADE)
    #profile=models.OneToOneField('Profile',on_delete=None)
    

class Agent_order(models.Model):
    transaction_code=models.CharField(max_length=255)
    #agent=models.ForeignKey("Agent",on_delete=None)
    delivered=models.BooleanField(default=False)
    castel=models.IntegerField(default=0)
    senq=models.IntegerField(default=0)
    doppel=models.IntegerField(default=0)
    george=models.IntegerField(default=0)
    total_payment=models.FloatField(default=0.0)
    #store=models.ForeignKey("Store",on_delete=None)
class Agent_store_manager(models.Model):
        username=models.CharField(max_length=50)
        password=models.CharField(max_length=255)
        email=models.CharField(max_length=50)
       # store=models.OneToOneField("Agent_store",on_delete=models.CASCADE)
       # profile=models.OneToOneField('Profile',on_delete=models.CASCADE)
    
class Agent_finance(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=255)
   # agent=models.ForeignKey("Agent",models.CASCADE)
   # profile=models.OneToOneField('Profile',on_delete=None)


