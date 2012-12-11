# -*- encoding: utf-8 -*-

# Importaciones del sistema 
from django.db.models import Q
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms.models import BaseModelFormSet
from django.forms.models import modelformset_factory
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt



# Se importa lo modelos de la aplicacion de bodega
from bodega.models import *

# Se importan los formularios 
from forms import ProductosForm, CategoriasForm, SubcategoriaForm, StatusForm, ProveedorForm, BodegaForm



@login_required
def venta(request):
	query = request.GET.get('q','')
	if query:
		qs = (
			Q(SKU__icontains=query) |
			Q(descripcion__icontains=query) |
			Q(categoria__nombre__icontains=query)		
		)
		results = Producto.objects.filter(qs).distinct()
	else:
		results = []
	return render_to_response('puntoventa/Consulta.html', {'results': results,'query': query }, context_instance=RequestContext(request))


@login_required
def categoria_simple(request, categoria_id):
	catego = get_object_or_404(Categoria, pk=categoria_id)
	productos = Producto.objects.filter(categoria_id=catego)
	return render_to_response('reports/categoria_simple.html', {'Categoria' : catego, 'productos' : productos}, context_instance=RequestContext
		(request))
	#return HttpResponse(productos)


@login_required
def EditarProducto(request, id):
    produ = get_object_or_404(Producto, pk=id)
    producto = Producto.objects.filter(id=produ)
    return HttpResponse(producto)

@login_required
def ListaCategorias(request):
    lista = Categoria.objects.all().order_by('nombre')
    #cuenta = Categoria.objects.filter(id=2).count()
    return render_to_response('reports/categoria.html', {'lista' :lista}, context_instance=RequestContext
		(request))



########################################## Vistas de formularios ##########################################


@csrf_exempt
@login_required
def addProductos(request):

    if request.method == 'POST':
        productosform = ProductosForm(request.POST)
        if productosform.is_valid():
            productosform.save()
            return HttpResponseRedirect('/categorias/')
    else:
        formset = ProductosForm()
    return render_to_response('puntoventa/addProducto.html', { 'formset': ProductosForm }, context_instance=RequestContext(request))

@csrf_exempt
@login_required
def addCategorias(request):

    if request.method == 'POST':
        # formulario enviado
        categoriasform = CategoriasForm(request.POST)

        if categoriasform.is_valid():
            # formulario validado correctamente
            categoriasform.save()
            return HttpResponseRedirect('/categorias/')

    else:
        # formulario inicial
        formset = CategoriasForm()

    return render_to_response('puntoventa/addProducto.html', { 'formset': CategoriasForm }, context_instance=RequestContext(request))


@csrf_exempt
@login_required
def addSubcategorias(request):

    if request.method == 'POST':
        # formulario enviado
        subcategoriasform = SubcategoriaForm(request.POST)

        if subcategoriasform.is_valid():
            # formulario validado correctamente
            subcategoriasform.save()
            return HttpResponseRedirect('/categorias/')

    else:
        # formulario inicial
        formset = SubcategoriaForm()

    return render_to_response('puntoventa/addProducto.html', { 'formset': SubcategoriaForm }, context_instance=RequestContext(request))


@csrf_exempt
@login_required
def addStatus(request):

    if request.method == 'POST':
        # formulario enviado
        statusform = StatusForm(request.POST)

        if statusform.is_valid():
            # formulario validado correctamente
            statusform.save()
            return HttpResponseRedirect('/categorias/')

    else:
        # formulario inicial
        formset = StatusForm()

    return render_to_response('puntoventa/addProducto.html', { 'formset': StatusForm }, context_instance=RequestContext(request))


@csrf_exempt
@login_required
def addProveedores(request):

    if request.method == 'POST':
        # formulario enviado
        proveedoresform = ProveedorForm(request.POST)

        if proveedoresform.is_valid():
            # formulario validado correctamente
            proveedoresform.save()
            return HttpResponseRedirect('/categorias/')

    else:
        # formulario inicial
        formset = ProveedorForm()

    return render_to_response('puntoventa/addProducto.html', { 'formset': ProveedorForm }, context_instance=RequestContext(request))


@csrf_exempt
@login_required
def addBodegas(request):

    if request.method == 'POST':
        # formulario enviado
        bodegasforms = BodegaForm(request.POST)

        if bodegasforms.is_valid():
            # formulario validado correctamente
            bodegasforms.save()
            return HttpResponseRedirect('/categorias/')

    else:
        # formulario inicial
        formset = BodegaForm()

    return render_to_response('puntoventa/addProducto.html', { 'formset': BodegaForm }, context_instance=RequestContext(request))
# Create your views here.
