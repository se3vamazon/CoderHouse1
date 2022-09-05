from django.urls import path 
from AppCoder.views import *


urlpatterns = [
    path('familiares/', viewfamiliares, name='AppCoderFamiliares'),
    path('', inicio, name = 'Inicio'),
    path('formulario/', formularioNombre, name = 'Formulario' ),
    path('busqueda/', busquedaFamiliar, name = 'Busqueda'),
    path('busquedaget/', busquedaFamiliarGet, name = 'BusquedaGet')
      
]