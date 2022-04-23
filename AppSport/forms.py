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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

