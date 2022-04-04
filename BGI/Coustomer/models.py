from django.db import models

# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=255)
    #agent=models.ForeignKey("Agent",on_delete=models.CASCADE)
    #profile=models.OneToOneField('Profile',on_delete=None)


class Customer_order(models.Model):
    transaction_code=models.CharField(max_length=255)
   # customer=models.ForeignKey("Agent",on_delete=None)
    delivered=models.BooleanField(default=False)
    castel=models.IntegerField()
    senq=models.IntegerField()
    doppel=models.IntegerField()
    george=models.IntegerField()
    total_payment=models.FloatField()
   # store=models.ForeignKey("Agent_store",on_delete=None)
