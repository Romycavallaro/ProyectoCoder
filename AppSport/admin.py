from django.contrib import admin
from .models import * #importamos el archivo models# 

admin.site.register(deporte)
admin.site.register(alumno)
admin.site.register(profesor)
admin.site.register(partido)