from django.db import models

# Create your models here.
class banda(models.Model):
	nombre = models.CharField(max_length=100)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

class grupo(models.Model):
	nombre = models.CharField(max_length=100)
	status = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.nombre
		
class emisora(models.Model):
	nombre = models.CharField(max_length=100)
	frecuencia = models.CharField(max_length=6,null=True)
	siglas = models.CharField(max_length=10,null=True)
	perfil = models.TextField(max_length=300,null=True)
	rating = models.DecimalField(max_digits=10,decimal_places=2)
	rating_tanget = models.DecimalField(max_digits=10,decimal_places=2)
	shere = models.DecimalField(max_digits=10,decimal_places=2)
	alcance = models.DecimalField(max_digits=10,decimal_places=2)
	alcance_tanget = models.DecimalField(max_digits=10,decimal_places=2)
	tafifa_publica = models.DecimalField(max_digits=10,decimal_places=2)
	grupo = models.ForeignKey(grupo)
	banda = models.ForeignKey(banda)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

class anunciosradio(models.Model):
	nombre = models.CharField(max_length=100)
	duracion = models.CharField(max_length=5,null=True)
	semanas = models.DecimalField(max_digits=10,decimal_places=2)
	dias = models.DecimalField(max_digits=10,decimal_places=2)
	emisora = models.ForeignKey(emisora)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

class campanaradio(models.Model):
	nombre = models.CharField(max_length=100)
	fecha_inicio = models.DateField(null=True)
	anuncios = models.ManyToManyField(anunciosradio,null=True)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

class productocliente(models.Model):
	nombre = models.CharField(max_length=100)
	campana = models.ForeignKey(campanaradio)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre

class cliente(models.Model):
	nombre = models.CharField(max_length=100)
	telefono = models.CharField(max_length=15,null=True)
	producto = models.ManyToManyField(productocliente,null=True)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre




