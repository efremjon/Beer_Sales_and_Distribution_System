from django.contrib import admin
from .models import Product,Profile,Store,Store_manager,Finance
# Register your models here.

class SelectFields(admin.ModelAdmin):
    fieldsets=(
        ('Name_stor', {'fields':('name')}),
        ('Product', {'fields': ('castel','senq','doppel','george')})   
    )

class BGI_Ethiopa(admin.AdminSite):
    site_header='BGI Ethiopa'
    site_title='Admin_site'
    index_title='BGI_Ethiopa'
BGI_Admin_site=BGI_Ethiopa(name='BGI_Ethiopa')

BGI_Admin_site.register(Product)
BGI_Admin_site.register(Profile)
BGI_Admin_site.register(Store)
BGI_Admin_site.register(Store_manager)
BGI_Admin_site.register(Finance)

admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(Store_manager)
admin.site.register(Finance)


