from django.contrib import admin
from bodega.models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('SKU', 'descripcion', 'categoria','subcategoria', 'precio', 'cantidad', 'bodega','status',)
    ordering = ['categoria',]
    search_fields = ['SKU', 'descripcion',]
    list_per_page =  75



class CategoriaAdmin(admin.ModelAdmin):
	pass

class SubcategoriaAdmin(admin.ModelAdmin):
	pass


class ProveedorAdmin(admin.ModelAdmin):
	pass


class BodegaAdmin(admin.ModelAdmin):
	pass

class StatusAdmin(admin.ModelAdmin):
	pass


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Bodega, BodegaAdmin)
admin.site.register(Status, StatusAdmin)
