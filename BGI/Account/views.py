from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Company.models import Customer ,Agent ,Finance ,Agent_finance,Agent_store_manager,Store_manager,Driver

# Create your views here.
#based on the request url ,we should decied who they are 
#login and session setting function and redirect to dashboard 
def login(request):
    if request.method == 'POST':
        if request.POST['password']!="" and request.POST['name']!="":
            username=request.POST['name']
            password=request.POST['password']
            user=Customer.objects.filter(username=username,password=password)
            if user:
                return HttpResponse('dash board')
            else:
                return HttpResponse('password or username is incorrect')
            
        else :
            return HttpResponse('no data')
    else:
        return HttpResponse('redirect to login')
