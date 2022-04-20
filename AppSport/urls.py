from django.contrib import admin
from django.urls import path
from AppSport import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('deportes', views.deportes, name="Deportes"),
    path('profesores', views.profesores, name="Profesores"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('partidos', views.partidos, name="Partidos"),
    path('formularioInscripcion', views.formularioInscripcion, name = "FormularioDeInscripcion"),
    ]