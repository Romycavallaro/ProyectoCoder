from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formularioInscripcion(forms.Form):
    nombreDelDeporte = forms.CharField(max_length=20)
    horario = forms.CharField(max_length=50)
    categoria = forms.IntegerField()

class leerResultados(forms.Form):
    fecha = forms.CharField(max_length=20)
    equipoRival = forms.CharField(max_length=20)
    resultadoFinal = forms.CharField(max_length=20)

class formularioPartidos(forms.Form):
    fecha = forms.CharField(max_length=20)
    equipoRival = forms.CharField(max_length=20)
    resultadoFinal = forms.CharField(max_length=20)
    ganado = forms.BooleanField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}