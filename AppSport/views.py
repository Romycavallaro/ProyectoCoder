from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import loader
from AppSport.models import Deporte, Alumno, Profesor, Partido
from AppSport.forms import formularioInscripcion, leerResultados



def deporte(self):
    deporte1 = Deporte(nombreDelDeporte= "Futbol", horario = "martes y sabado de 13 a 14 Hs", categoria=2017)
    deporte1.save()

    deporte2 = Deporte(nombreDelDeporte = "Basquet", horario = "martes y viernes de 10 a 11 Hs", categoria=2005)
    deporte2.save()

    deporte3 = Deporte(nombreDelDeporte = "Hockey", horario = "miércoles y viernes de 17 a 18 Hs", categoria=2003)
    deporte3.save()

    deporte4 = Deporte(nombreDelDeporte = "Voley", horario = "lunes y jueves de 18 a 19 Hs", categoria=2010)
    deporte4.save()

    documentoDeTexto = f"--->Deporte:{deporte1.nombreDelDeporte}, Horario:{deporte1.horario}, Edad:{deporte1.categoria}" + f"--->Deporte:{deporte2.nombreDelDeporte}, Horario:{deporte2.horario}, Edad:{deporte2.categoria}" + f"--->Deporte:{deporte3.nombreDelDeporte}, Horario:{deporte3.horario}, Edad:{deporte3.categoria}" + f"--->Deporte:{deporte4.nombreDelDeporte}, Horario:{deporte4.horario}, Edad:{deporte4.categoria}"
    return HttpResponse(documentoDeTexto)


def alumno(self):
    alumno1 = Alumno(nombre = "Dante", apellido = "Garegnani", categoria=2017)
    alumno1.save()

    alumno2 = Alumno(nombre = "Antonio", apellido = "Cavagnani", categoria=2010)
    alumno2.save()

    alumno3 = Alumno(nombre = "Sienna", apellido = "Martinez", categoria=2006)
    alumno3.save()

    documentoDeTexto = f"--->Nombre:{alumno1.nombre}, Apellido:{alumno1.apellido}, Categoria:{alumno1.categoria}" + f"--->Nombre:{alumno2.nombre}, Apellido:{alumno2.apellido}, Categoria:{alumno2.categoria}" + f"--->Nombre:{alumno3.nombre}, Apellido:{alumno3.apellido}, Categoria:{alumno3.categoria}"
    return HttpResponse(documentoDeTexto)


def profesor(self):
    profesor1 = Profesor(nombre = "Alejandro", apellido = "Fernandez", deporte = "Futbol")
    profesor1.save()

    profesor2 = Profesor(nombre = "Marcela", apellido = "LOpez", deporte = "Voley")
    profesor2.save()

    profesor3 = Profesor(nombre = "Irina", apellido = "Gonzalez", deporte = "Hockey")
    profesor3.save()

    profesor4 = Profesor(nombre = "Martina", apellido = "Lombardi", deporte = "Basquet")
    profesor4.save()

    documentoDeTexto = f"--->Nombre:{profesor1.nombre}, Apellido:{profesor1.apellido}, Deporte:{profesor1.deporte}" + f"--->Nombre:{profesor2.nombre}, Apellido:{profesor2.apellido}, Deporte:{profesor2.deporte}" + f"--->Nombre:{profesor3.nombre}, Apellido:{profesor3.apellido}, Deporte:{profesor3.deporte}" + f"--->Nombre:{profesor4.nombre}, Apellido:{profesor4.apellido}, Deporte:{profesor4.deporte}"
    return HttpResponse(documentoDeTexto)


def partido(self):
    partido1 = Partido(fecha = "2022-04-01", equipoRival = "San Lorenzo", resultadoFinal = "2 a 1", ganado = True)
    partido1.save()

    partido2 = Partido(fecha = "2022-04-12", equipoRival = "River", resultadoFinal = "4 a 0", ganado = True)
    partido2.save()

    partido3 = Partido(fecha = "2022-04-17", equipoRival = "Arsenal", resultadoFinal = "1 a 1", ganado = False)
    partido3.save()

    documentoDeTexto = f"--->Fecha:{partido1.fecha}, El Equipo Rival fue:{partido1.equipoRival}, El resultado fue:{partido1.resultadoFinal}, EL partido fue ganado:{partido1.ganado}" + f"--->Fecha:{partido2.fecha}, El Equipo Rival fue:{partido2.equipoRival}, El resultado fue:{partido2.resultadoFinal}, EL partido fue ganado:{partido2.ganado}" + f"--->Fecha:{partido3.fecha}, El Equipo Rival fue:{partido3.equipoRival}, El resultado fue:{partido3.resultadoFinal}, EL partido fue ganado:{partido3.ganado}"
    return HttpResponse(documentoDeTexto)


def inicio(request):
    return render(request, 'inicio.html')

def deportes(request):
    return render(request, 'deportes.html')

def alumnos(request):
    return render(request, 'alumnos.html')

def profesores(request):
    return render(request, 'profesores.html')

def partidos(request):
    return render(request, 'partidos.html')

def formularioDeInscripcion(request):
    if request.method == "POST":
        
        miFormulario = formularioInscripcion(request.POST) 
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            infoDeporte = Deporte(
                nombreDelDeporte=informacion["nombreDelDeporte"], horario=informacion["horario"], categoria=informacion["categoria"])
            infoDeporte.save()
            return render(request, 'inicio.html')

    else: 
            miFormulario = formularioInscripcion()
        
    return render(request, 'formularioInscripcion.html', {"miFormulario" : miFormulario})


def busquedaDeporte(request):
    return render(request, 'busquedaDeporte.html')

def buscar(request):
    respuesta = f"Estoy buscando el Deporte: {request.GET['deporte']}"
    return HttpResponse(respuesta)

def partidos(request):
    if request.method == 'POST':

        miFormulario = partidosFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid: 
            informacion = miFormulario.cleaned_data
            infoPartido = Partido(
                fecha=informacion['fecha'], equipoRival=informacion['EquipoRIval'],resultadoFinal=informacion['resultadoFinal'], ganado=informacion['Ganado'])
            profesor.save()
            return render(request, 'inicio.html') 

    else:
        miFormulario= partidosFormulario() 
    
    return render(request, 'partidos.html', {"miFormulario":miFormulario})

def leerLosResultados(request):
    resultado = Partido.objects.all() 
    contexto= {"partidos":partidos}
    return render(request, 'leerResultados.html', contexto)
     