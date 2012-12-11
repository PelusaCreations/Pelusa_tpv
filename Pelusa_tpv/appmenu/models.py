from django.db import models

class MenusApp(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=255, unique=True, help_text='Ingresa el identificador de la url')
	url = models.URLField(max_length=200, verify_exists=False)


	def __unicode__(self):
		return self.nombre

