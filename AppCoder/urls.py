from django.urls import path 
from AppCoder.views import viewfamiliares, inicio


urlpatterns = [
    path('entregable/', viewfamiliares, name='AppCoderFamiliares'),
    path('', inicio),
    
]