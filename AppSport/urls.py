from django.contrib import admin
from django.urls import path
from AppSport import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('deportes', views.deportes, name="Deportes"),
    path('profesores', views.profesores, name="Profesores"),
    path('alumnos', views.alumnos, name="Alumnos"),
    path('partidos', views.partido, name="Partidos"),
    path('formularioInscripcion', views.formularioDeInscripcion, name = "FormularioDeInscripcion"),
    path('busquedaDeporte', views.busquedaDeporte, name="BusquedaDeporte"),
    path('buscar/', views.buscar),
    path('leerResultados', views.leerLosResultados, name = "LeerLosResultados"),
    path('resultadosPartido', views.resultadosPartidos, name = "resultadosPartido"),
    path('eliminarResultado/<partido_fecha>/', views.eliminarLosResultados, name="EliminarResultado"),
    path('editarResultado/<partido_equipoRival>/', views.editarResultado, name="EditarResultado"),
    path('deporte/list', views.DeporteList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.DeporteDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.DeporteCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.DeporteUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.DeporteDelete.as_view(), name='Delete'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
    ]