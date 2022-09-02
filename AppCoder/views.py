from ast import AsyncFunctionDef
from django.shortcuts import render
from AppCoder.forms import Formulario
from AppCoder.models import Familiares
import datetime

# Create your views here.

def viewfamiliares(request):
    familiar1 = Familiares(nombre= 'Seba', edad = 29)
    familiar2 = Familiares(nombre= 'Emma', edad = 29)
    familiar3 = Familiares(nombre = 'Andy', edad =  26)
    familiar1.save()
    familiar2.save()
    familiar3.save()

    contexto = {
        'familiar1': familiar1,
        'familiar2' : familiar2,
        'familiar3' : familiar3,
    }
    return render(request, 'AppCoder/familia.html', contexto)


def inicio(request):

    return render(request, 'index.html')

def formularioNombre(request):

    if request.method == 'POST':
        miFormulario = Formulario(request.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            nombre1 = Familiares(nombre=data.get('nombre'), edad=data.get('edad'))
            nombre1.save()

    
    
    contexto = {
        'form': Formulario()
    }

    return render(request, "AppCoder/formulario.html", contexto)
