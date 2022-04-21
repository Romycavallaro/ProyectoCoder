from django import forms

class formularioInscripcion(forms.Form):
    deporte = forms.CharField()
    categoria = forms.IntegerField()

class leerResultados(forms.Form):
    deporte = forms.CharField(max_length=20)
    fecha = forms.CharField(max_length=20)
    equipoRival = forms.CharField(max_length=20)
    resultadoFinal = forms.CharField(max_length=20)


