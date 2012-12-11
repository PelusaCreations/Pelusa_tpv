# -*- encoding: utf-8 -*-

# Importaciones del sistema 
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Se importa lo modelos de la aplicacion de bodega
from Pelusa_tpv.appmenu.models import MenusApp

@login_required
def Nav(request):
	menuapp = MenusApp.objects.all().order_by('nombre')
	return render_to_response('puntoventa/Consulta.html', {'menuapp' :menuapp}, context_instance=RequestContext
		(request))