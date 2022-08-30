from django.urls import path 
from AppCoder.views import viewfamiliares, inicio


urlpatterns = [
    path('familiares/', viewfamiliares, name='AppCoderFamiliares'),
    path('', inicio, name = 'Inicio'),
    
]