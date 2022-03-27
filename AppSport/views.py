from django.shortcuts import render
from django.http import HttpResponse
from AppSport.models import Deporte

def Deporte(self):
    deporte = Deporte(nombre = "Futbol", horario = "martes y sabado de 13 a 14 Hs", edad=5)
    deporte.save()
    documentoDeTexto = f"--->Deporte:{deporte.nombre}, Horario:{deporte.horario}, Edad:{deporte.edad}"
    return HttpResponse(documentoDeTexto)




