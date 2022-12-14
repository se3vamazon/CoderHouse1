from ast import AsyncFunctionDef
from django.shortcuts import render, redirect
from AppCoder.forms import BusquedaNombreForm, Formulario, Paciente
from AppCoder.models import Familiares, Pacientes
import datetime

# Create your views here.

def viewfamiliares(request):
    familia = Familiares.objects.all()

    contexto = {
        'familia' : familia
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

            return redirect ('AppCoderFamiliares')

    familia = Familiares.objects.all()

    
    
    contexto = {
        'form': Formulario(),
        'familia' : familia,
    }

    return render(request, "AppCoder/formulario.html", contexto)

def busquedaFamiliarGet(request):
    nombre = request.GET.get('nombre')

    filtrados = Familiares.objects.filter(nombre__exact =nombre)

    contexto = {
        'filtrados' : filtrados
    }
    
    return render(request, "AppCoder/nombrefiltrado.html", contexto)

def busquedaFamiliar(request):

    contexto = {
        'form': BusquedaNombreForm()
    }

    return render(request, "AppCoder/busqueda.html", contexto)

def agregaPaciente(request):
    if request.method == 'POST':
        miPaciente = Paciente(request.POST)
        
        if miPaciente.is_valid():
            data = miPaciente.cleaned_data

            nombre1 = Pacientes(nombre=data.get('nombre'), DNI=data.get('DNI'))
            nombre1.save()

            return redirect ('AgregaPaciente')

    pacientes = Pacientes.objects.all() 
    
    contexto = {
        'form': Paciente(),
        'pacientes' : pacientes,
    }

    return render(request, "AppCoder/paciente.html", contexto)

