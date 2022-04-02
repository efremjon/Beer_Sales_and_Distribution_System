from django.contrib import admin
from .models import Agent,Agent_finance,Agent_order,Agent_store,Finance,Agent_store_manager,Store,Store_manager,Customer,Customer_order,Product,Profile,Region,Driver

# Register your models here.
admin.site.register(Finance)
admin.site.register(Store)
admin.site.register(Store_manager)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Region)
admin.site.register(Agent)
admin.site.register(Agent_order)
admin.site.register(Agent_store)
admin.site.register(Agent_store_manager)
admin.site.register(Agent_finance)
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(Customer_order)

