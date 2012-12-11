# -*- encoding: utf-8 -*-
from django import forms
from models import Producto, Categoria, Subcategoria, Status, Proveedor, Bodega


class ProductosForm(forms.ModelForm):
	class Meta:
		model = Producto


class CategoriasForm(forms.ModelForm):
	class Meta:
		model = Categoria

class SubcategoriaForm(forms.ModelForm):
	class Meta:
		model = Subcategoria

class StatusForm(forms.ModelForm):
	class Meta:
		model = Status

class ProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor

class BodegaForm(forms.ModelForm):
	class Meta:
		model = Bodega