# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Producto.fecha_ingreso'
        db.alter_column('bodega_producto', 'fecha_ingreso', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Changing field 'Producto.fecha_ingreso'
        db.alter_column('bodega_producto', 'fecha_ingreso', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'bodega.bodega': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Bodega'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bodega.categoria': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Categoria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'bodega.producto': {
            'Meta': {'object_name': 'Producto'},
            'SKU': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'bodega': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bodega.Bodega']"}),
            'cantidad': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bodega.Categoria']"}),
            'codigo_barras': ('django.db.models.fields.IntegerField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fecha_ingreso': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'precio_compra': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'precio_especial': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'precio_mayoreo': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bodega.Proveedor']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bodega.Status']"}),
            'subcategoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bodega.Subcategoria']"})
        },
        'bodega.proveedor': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Proveedor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'bodega.status': {
            'Meta': {'object_name': 'Status'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        'bodega.subcategoria': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Subcategoria'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bodega.Categoria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['bodega']
