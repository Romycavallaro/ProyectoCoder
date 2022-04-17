from django.contrib import admin
from django.urls import path
from AppSport import views
from AppSport.views import titulo, Template, deporte, alumno, profesor, partido

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('deporte', views.deporte, name="Deportes"),
    path('profesor', views.profesores, name="Profesores"),
    path('alumno', views.alumnos, name="Alumnos"),
    path('partido', views.partido, name="Partidos"),
    path('titulo/', titulo),
    path('template/', Template),
    path('deporte/', deporte),
    path('alumno/', alumno),
    path('profesor/', profesor),
    path('partido/', partido),
    path('formularioInscripcion/', views.formularioInscripcion, name = "Formulario de Inscripcion"),
    path('busquedaDeporte/', views.busquedaDeporte, name = 'BusquedaDeporte'),
    path('buscar/', views.buscar),
    ]
