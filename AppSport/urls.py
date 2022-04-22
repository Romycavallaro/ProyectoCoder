from django.contrib import admin
from django.urls import path
from AppSport import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('deportes', views.deportes, name="Deportes"),
    path('profesores', views.profesores, name="Profesores"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('partidos', views.partidos, name="Partidos"),
    path('formularioInscripcion', views.formularioDeInscripcion, name = "FormularioDeInscripcion"),
    path('busquedaDeporte', views.busquedaDeporte, name="BusquedaDeporte"),
    path('buscar/', views.buscar),
    path('leerResultados', views.leerLosResultados, name = "LeerLosResultados"),
    path('eliminarResultado/<partido_fecha>/', views.eliminarLosResultados, name="EliminarResultado"),
    path('editarResultado/<partido_fecha>/', views.editarResultado, name="EditarResultado"),
    path('deporte/list', views.DeporteList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.DeporteDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.DeporteCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.DeporteUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.DeporteDelete.as_view(), name='Delete'),
    ]