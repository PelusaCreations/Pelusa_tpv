from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^csl/', 'bodega.views.venta'),
    url(r'^categorias/', 'bodega.views.ListaCategorias'),
    url(r'^categoria/(?P<categoria_id>\d+)$', 'bodega.views.categoria_simple'),
    url(r'^addproducto/', 'bodega.views.addProductos'),
    url(r'^addcategoria/', 'bodega.views.addCategorias'),
    url(r'^addsubcategoria/', 'bodega.views.addSubcategorias'),
    url(r'^addstatus/', 'bodega.views.addStatus'),
    url(r'^addproveedor/', 'bodega.views.addProveedores'),
    url(r'^addbodega/', 'bodega.views.addBodegas'),
    url(r'^producto/(?P<id>\d+)$', 'bodega.views.EditarProducto'),
    

    url(r'^reporte/productos/', 'reportes.views.ReportesProductos'),
    url(r'^reporte/categorias/(?P<categoria_id>\d+)$', 'reportes.views.ReporteCategorias'),


    url(r'^administracion/nuevousuario/', 'usuarios.views.NuevoUsuario'),


    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/login.html'}),
    url(r'^', 'django.contrib.auth.views.login', name='home'),




)


if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns