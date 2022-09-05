from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()

class Pacientes(models.Model):
    nombre = models.CharField(max_length=20)
    DNI = models.IntegerField()

class Medico(models.Model):
    medico = models.CharField(max_length=20)
    matricla = models.IntegerField()


