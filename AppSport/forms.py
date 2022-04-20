from django import forms

class formularioInscripcion(forms.Form):
    deporte = forms.CharField()
    categoria = forms.IntegerField()