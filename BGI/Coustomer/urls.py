from django.urls import path
from .import views

urlpatterns =[
    path('',views.home,name='home'),
    path('Customer_Order/',views.Cust_order,name='Cust_order'),
]