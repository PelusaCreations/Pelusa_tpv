from django.db import models
from django.contrib import admin


class Categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	def  __unicode__(self):
		return self.nombre
	class Meta():
		ordering = ['nombre']

class Subcategoria(models.Model):
	categoria = models.ForeignKey('Categoria')
	nombre = models.CharField(max_length=100, unique=True)
	def  __unicode__(self):
		return self.nombre
	class Meta():
		ordering = ['nombre']


class Proveedor(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	def __unicode__(self):
		return self.nombre
	class Meta():
		ordering = ['nombre']

class Bodega(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	ubicacion = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre
	class Meta():
		ordering = ['nombre']


class Status(models.Model):
	status = models.CharField(max_length=10, unique=True)
	def __unicode__(self):
		return self.status

		
class Producto(models.Model):
	SKU = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=50)
	slug = models.SlugField(max_length=255, unique=True, help_text='Unique value for product page URL, created from name.')
	categoria = models.ForeignKey('Categoria')
	subcategoria = models.ForeignKey('Subcategoria')
	cantidad = models.IntegerField(max_length=1000)
	codigo_barras = models.IntegerField(max_length=200, unique=True, null=True, blank=True)
	precio = models.DecimalField(max_digits=5, decimal_places=2)
	precio_especial = models.DecimalField(max_digits=5, decimal_places=2)
	precio_compra = models.DecimalField(max_digits=5, decimal_places=2)
	precio_mayoreo = models.DecimalField(max_digits=5, decimal_places=2)
	fecha_ingreso = models.DateTimeField(auto_now_add=True)
	proveedor = models.ForeignKey('Proveedor')
	bodega = models.ForeignKey('Bodega')
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion 




