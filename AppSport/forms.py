from django import forms

class formularioInscripcion(forms.Forms):
    deporte = forms.CharField()
    categoria = forms.IntegerField()