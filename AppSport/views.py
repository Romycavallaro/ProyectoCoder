from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import loader
from AppSport.models import Deporte, Alumno, Profesor, Partido


def titulo(request):
    return HttpResponse("App Sport")

def Template(self):

    titulo = "App Sport"
    descripcion = "Una App creada por el club para que encuentres tu pasión por el deporte"

    diccionario = {"titulo": titulo, "descripcion": descripcion}
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)


def deporte(self):
    deporte1 = Deporte(nombre = "Futbol", horario = "martes y sabado de 13 a 14 Hs", edad=5)
    deporte1.save()

    deporte2 = Deporte(nombre = "Basquet", horario = "martes y viernes de 10 a 11 Hs", edad=6)
    deporte2.save()

    deporte3 = Deporte(nombre = "Hockey", horario = "miércoles y viernes de 17 a 18 Hs", edad=7)
    deporte3.save()

    deporte4 = Deporte(nombre = "Voley", horario = "lujes y jueves de 18 a 19 Hs", edad=10)
    deporte4.save()

    documentoDeTexto = f"--->Deporte:{deporte1.nombre}, Horario:{deporte1.horario}, Edad:{deporte1.edad}" + f"--->Deporte:{deporte2.nombre}, Horario:{deporte2.horario}, Edad:{deporte2.edad}" + f"--->Deporte:{deporte3.nombre}, Horario:{deporte3.horario}, Edad:{deporte3.edad}" + f"--->Deporte:{deporte4.nombre}, Horario:{deporte4.horario}, Edad:{deporte4.edad}"
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
    return render(request, 'AppSport/inicio.html')

def deportes(request):
    return render(request, 'AppSport/deportes.html')

def alumnos(request):
    return render(request, 'AppSport/alumnos.html')

def profesores(request):
    return render(request, 'AppSport/profesores.html')

def partidos(request):
    return render(request, 'AppSport/partidos.html')

def formularioInscripcion(request):

    if request.method == 'post':
        miFormulario = formularioInscripcion(request.post)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

        deporte = deporte (request.post ['deporte'], request.post ['categoria'])
        deporte.save()
        return render(request, 'AppSport/inicio.html')

    else:
        miFormulario = formularioInscripcion()
        return render(request, 'AppSport/formularioInscripcion.html')


def busquedaDeporte(request):
    return render(request, 'AppSport/busquedaDeporte.html')

def buscar(request):

    if request.get ['deporte']:
        deporte = request.get ['deporte']
        deporte = deporte.objects.filter(deporte_icontains = deporte)

        return render(request, 'AppSport/resultadoBusqueda.html', {deporte : deporte})
    
    else: 
        respuesta = "No has enviado datos"
    
    return HttpResponse(repuesta)
