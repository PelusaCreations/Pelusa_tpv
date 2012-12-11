# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required


 ## Se importan las clases de Geraldo reports

from geraldo.generators import PDFGenerator
from geraldo import Report, ReportBand, DetailBand, SystemField, Label, ObjectValue
from geraldo.utils import cm, BAND_WIDTH, TA_CENTER, TA_RIGHT

##   Se importan los modelos de bodega   ##
##   de donde se toma la informacion     ##
##   para sacar los reportes		     ##

from bodega.models import *

class ReportProducto(Report):
    title = 'Reporte de Productos'

    class band_detail(DetailBand):
        height = 0.5*cm
        elements = [
            ObjectValue(expression='SKU', left=0.5*cm, top=0.2*cm, style={'fontSize': 6}),
            ObjectValue(expression='descripcion', left=3*cm, top=0.2*cm, style={'fontSize': 6}),
            ObjectValue(expression='categoria', left=12.0*cm, top=0.2*cm, style={'fontSize': 6}),
			ObjectValue(expression='cantidad', left=10*cm, top=0.2*cm, style={'fontSize': 6}),
            ObjectValue(expression='precio', left=8.0*cm, top=0.2*cm, style={'fontSize': 6}),

        ]
        borders = {'all': False}

    class band_page_header(ReportBand):
        height = 1.3*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                style={'fontName': 'Helvetica-Bold', 'fontSize': 12, 'alignment': TA_CENTER}),
            Label(text="SKU", top=0.8*cm, left=0.5*cm, style={'fontSize': 6}),
            Label(text="Producto", top=0.8*cm, left=3*cm, style={'fontSize': 6}),
            Label(text="Categoria", top=0.8*cm, left=12.0*cm, style={'fontSize': 6}),
            Label(text="Cantidad", top=0.8*cm, left=9.5*cm, style={'fontSize': 6}),
            Label(text="Precio Publico", top=0.8*cm, left=7.5*cm, style={'fontSize': 6})
        ]
        borders = {'all': True}


    class band_page_footer(ReportBand):
        height = 0.5*cm
        elements = [
            Label(text='JueguetyFiesta', top=0.1*cm),

            SystemField(expression='Reporte del  %(now:%Y, %b %d)s a las %(now:%H:%M)s', top=0.1*cm,
                width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
            ]
        borders = {'top': True}

    class band_summary(ReportBand):
        height = 0.5*cm
        elements = [
          Label(text='Productos Totales:',  top=0.5*cm, left=0.5*cm),
          ObjectValue(expression='sum(cantidad)', left=3.5*cm, top=0.5*cm),
        ]
        borders = {'top': True}


@login_required
def ReportesProductos(request):
	resp = HttpResponse(mimetype='application/pdf')

	productos = Producto.objects.all()
	report = ReportProducto(queryset=productos)
	report.generate_by(PDFGenerator, filename=resp)

	return resp


@login_required
def ReporteCategorias(request, categoria_id):
    resp = HttpResponse(mimetype='application/pdf')
    catego = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria_id=catego)
    report = ReportProducto(queryset=productos)
    report.generate_by(PDFGenerator, filename=resp)
    
    return resp