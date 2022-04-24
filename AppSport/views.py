from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import loader
from AppSport.models import Deporte, Alumno, Profesor, Partido
from AppSport.forms import formularioInscripcion, leerResultados, UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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

def partido(request):
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

        miFormulario2 = partidosFormulario(request.POST)
        print(miFormulario2)
        
        if miFormulario2.is_valid: 
            informacion = miFormulario2.cleaned_data
            infoPartido = Partido(
                fecha=informacion['fecha'], equipoRival=informacion['EquipoRIval'],resultadoFinal=informacion['resultadoFinal'])
            infoPartido.save()
            return render(request, 'inicio.html') 

    else:
        miFormulario2= partidosFormulario() 
    
    return render(request, 'leerResultados.html', {"miFormulario2":miFormulario2})

def leerLosResultados(request):
    resultado = Partido.objects.all() 
    contexto= {"partidos": resultado}
    return render(request, 'leerResultados.html', contexto)

def eliminarLosResultados(request, partido_fecha):
    infoPartido = Partido.objects.get(fecha=partido_fecha)
    infoPartido.delete()
    
    resultado = Partido.objects.all() 
    contexto = {"partidos": resultado}
    return render(request, 'leerResultados.html', contexto)

def editarResultado(request, partido_fecha):
    infoPartido = Partido.objects.get(fecha=partido_fecha)
    if request.method == 'POST':
        
        miFormulario3 = partidosFormulario(request.POST)
        print(miFormulario3)
        if miFormulario3.is_valid:  
            informacion = miFormulario3.cleaned_data
            partido.fecha = informacion['fecha']
            partido.equipoRival = informacion['equipoRival']
            partido.resultadoFinal = informacion['resultadoFinal']
            partido.save()
            
            return render(request, 'inicio.html')

    else:
    
        miFormulario3 = partidosFormulario(initial={'fecha': partido.fecha, 'equipoRival': partido.equipoRival,
                                                   'resultadoFinal': partido.resultadoFinal})
    
    return render(request, 'editarResultado.html', {"miFormulario3": miFormulario3, "partido_fecha": partido_fecha})

class DeporteList(ListView):
    model = Deporte
    template_name = 'deportes_list.html'

class DeporteDetalle(ListView): 
    model = Deporte
    template_name = 'deporte_detalle.html'    

class DeporteCreacion(CreateView):
    model = Deporte
    success_url = 'deporte/list'
    fields = ['nombre', 'horario', 'categoria']

class DeporteUpdate(UpdateView):
    model = Deporte
    success_url = 'deporte/list'
    fields = ['nombre', 'horario', 'categoria']

class DeporteDelete(DeleteView):
    model = Deporte
    success_url = 'deporte/list'

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid(): 
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            
            if user is not None:
                login(request, user)
                return render(request, 'inicio.html', {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request, 'inicio.html', {"mensaje":"Datos incorrectos"})
        
        else:
            return render(request, 'inicio.html', {"mensaje":"Formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

def register(request):
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,'inicio.html' , {"mensaje":"Usuario Creado :)"})
        
        else:
            form = UserCreationForm()
            form = UserRegisterForm()
        
        return render(request,'registro.html' , {"form":form})

@login_required
def inicio(request):
    return render(request,'inicio.html')

@login_required
def editarPerfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            
            return render(request, 'inicio.html')
        
        else:
            miFormulario = UserEditForm(initial={'email': usuario.email})
        
        return render(request, 'editarPerfil.html', {"miFormulario": miFormulario, "usuario": usuario})

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'inicio.html', {"url": avatares[0].imagen.url})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid:
            u = user.objects.get(username = request.user)
            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'inicio.html')
    
    else:
        miFormulario = AvatarFormulario()
    
    return render(request, 'agregarAvatar.html', {"miFormulario": miFormulario}) 