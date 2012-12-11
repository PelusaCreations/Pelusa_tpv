# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Categoria'
        db.create_table('bodega_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('bodega', ['Categoria'])

        # Adding model 'Subcategoria'
        db.create_table('bodega_subcategoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bodega.Categoria'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('bodega', ['Subcategoria'])

        # Adding model 'Proveedor'
        db.create_table('bodega_proveedor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('bodega', ['Proveedor'])

        # Adding model 'Bodega'
        db.create_table('bodega_bodega', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bodega', ['Bodega'])

        # Adding model 'Status'
        db.create_table('bodega_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
        ))
        db.send_create_signal('bodega', ['Status'])

        # Adding model 'Producto'
        db.create_table('bodega_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('SKU', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bodega.Categoria'])),
            ('subcategoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bodega.Subcategoria'])),
            ('cantidad', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('codigo_barras', self.gf('django.db.models.fields.IntegerField')(max_length=200, unique=True, null=True, blank=True)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('precio_especial', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('precio_compra', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('precio_mayoreo', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateTimeField')()),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bodega.Proveedor'])),
            ('bodega', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bodega.Bodega'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bodega.Status'])),
        ))
        db.send_create_signal('bodega', ['Producto'])


    def backwards(self, orm):
        
        # Deleting model 'Categoria'
        db.delete_table('bodega_categoria')

        # Deleting model 'Subcategoria'
        db.delete_table('bodega_subcategoria')

        # Deleting model 'Proveedor'
        db.delete_table('bodega_proveedor')

        # Deleting model 'Bodega'
        db.delete_table('bodega_bodega')

        # Deleting model 'Status'
        db.delete_table('bodega_status')

        # Deleting model 'Producto'
        db.delete_table('bodega_producto')


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
            'fecha_ingreso': ('django.db.models.fields.DateTimeField', [], {}),
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
