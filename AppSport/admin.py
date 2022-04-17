from django.contrib import admin
from .models import * #importamos el archivo models# 

admin.site.register(Deporte)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Partido)