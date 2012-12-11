from django.contrib import admin
from Pelusa_tpv.appmenu.models import MenusApp

class MenusAppAdmin(admin.ModelAdmin):
    ordering = ['nombre',]
    search_fields = ['nombre', 'url',]
    list_per_page =  10

admin.site.register(MenusApp, MenusAppAdmin)
