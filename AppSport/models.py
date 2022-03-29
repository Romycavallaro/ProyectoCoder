from django.db import models

# Create your models here.
class deporte(models.Model):
    nombre = models.CharField(max_length=20)
    horario = models.CharField(max_length=50)
    edad = models.IntegerField()

class alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    categoria = models.IntegerField()

class profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    deporte = models.CharField(max_length=100)

class partido(models.Model):
    fecha = models.DateField()
    equipoRival = models.CharField(max_length=20)
    resultadoFinal = models.IntegerField()
    ganado = models.BooleanField()