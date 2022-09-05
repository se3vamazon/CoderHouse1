from django import forms

from AppCoder.models import Familiares

class Formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class BusquedaNombreForm(forms.Form):
    nombre = forms.CharField()

class Paciente(forms.Form):
    nombre = forms.CharField()
    DNI = forms.IntegerField()



    

