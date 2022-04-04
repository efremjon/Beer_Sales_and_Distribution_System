import site
from django.contrib import admin
from .models import Agent,Agent_finance,Agent_order,Agent_store,Agent_store_manager
# Register your models here.

class AgentAdmin(admin.AdminSite):
    site_header='Agent Admin-Area'
    site_title='Admin_Aite'
    index_title='Agent_Dashbord'
Agent_site=AgentAdmin(name='Agent_Admin')

Agent_site.register(Agent)
Agent_site.register(Agent_finance)
Agent_site.register(Agent_order)
Agent_site.register(Agent_store)
Agent_site.register(Agent_store_manager)

# this for super admin

admin.site.register(Agent)
admin.site.register(Agent_finance)
admin.site.register(Agent_order)
admin.site.register(Agent_store)
admin.site.register(Agent_store_manager)

