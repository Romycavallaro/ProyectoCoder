from django import forms

class formularioInscripcion(forms.Form):
    nombreDelDeporte = forms.CharField(max_length=20)
    horario = forms.CharField(max_length=50)
    categoria = forms.IntegerField()

class leerResultados(forms.Form):
    fecha = forms.CharField(max_length=20)
    equipoRival = forms.CharField(max_length=20)
    resultadoFinal = forms.CharField(max_length=20)


