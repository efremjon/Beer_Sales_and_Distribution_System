from django.shortcuts import render

def home(request):
    return render(request,'Coustomer/home.html',{})

def login(request):
    return render(request,'')