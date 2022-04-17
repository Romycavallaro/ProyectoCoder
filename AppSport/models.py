from django.db import models

# Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length=20)
    horario = models.CharField(max_length=50)
    edad = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    categoria = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    deporte = models.CharField(max_length=100)

class Partido(models.Model):
    fecha = models.DateField()
    equipoRival = models.CharField(max_length=20)
    resultadoFinal = models.CharField(max_length=20)
    ganado = models.BooleanField()