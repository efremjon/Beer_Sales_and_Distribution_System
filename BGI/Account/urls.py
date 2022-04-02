from django.urls import path
from django.views.generic import TemplateView
from .views import login


urlpatterns=[
    path('',TemplateView.as_view(template_name="Registration/index.html"),name='login'),
     path('register/',TemplateView.as_view(template_name="Registration/register.html"),name="register"),
     path('login/',login,name="login_btn")
   
]