
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('Agent/',include('Agent.urls')),
    path('BGI/',include('Company.urls')),
    path('Coustomer/',include('Coustomer.urls')),
]
