from django.urls import path 
from AppCoder.views import formularioNombre, viewfamiliares, inicio, formularioNombre


urlpatterns = [
    path('familiares/', viewfamiliares, name='AppCoderFamiliares'),
    path('', inicio, name = 'Inicio'),
    path('formulario/', formularioNombre, name = 'Formulario' )
    
]