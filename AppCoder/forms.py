from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()