from django.shortcuts import render

def home(request):
    return render(request,'Customer/home.html',{})

def Cust_order(request):
    return render(request,'Customer/customer_order.html',{})


def login(request):
    return render(request,'')