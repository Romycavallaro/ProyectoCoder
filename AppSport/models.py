from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deporte(models.Model):
    nombreDelDeporte = models.CharField(max_length=20)
    horario = models.CharField(max_length=50)
    categoria = models.IntegerField()

    def __str__(self):
        return f"Deporte: {self.nombreDelDeporte} - Horario de practica {self.horario} - Edad para participar {self.categoria}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    categoria = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Categoria {self.categoria}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    deporte = models.CharField(max_length=100)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Deporte {self.deporte}"

class Partido(models.Model):
    fecha = models.DateField()
    equipoRival = models.CharField(max_length=20)
    resultadoFinal = models.CharField(max_length=20)
    ganado = models.BooleanField(null=True)

    def __str__(self):
        return f"Fecha: {self.fecha} - Equipo Rival {self.equipoRival} - Resultado Final {self.resultadoFinal}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"