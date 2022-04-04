
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from Agent.admin import Agent_site
from Company.admin import BGI_Admin_site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Agent-Admin/', Agent_site.urls),
    path('BGI-Admin/',BGI_Admin_site.urls),
    path('',include('Home.urls')),
    path('Agent/',include('Agent.urls')),
    path('BGI/',include('Company.urls')),
    path('Coustomer/',include('Coustomer.urls')),
]

admin.site.index_title="BGI-Ethiopan"
admin.site.site_header="BGI-Ethiopan"
admin.site.site_title="Admin-Dashbord"