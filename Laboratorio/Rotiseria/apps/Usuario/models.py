from enum import unique
from re import S
from tkinter import CASCADE
from django.db import models


# Create your models here.
class ZonaDomicilio(models.Model):
    cod_zona = models.AutoField(primary_key=True)
    descripcion_zona = models.CharField(max_length=200,blank= True)



class Domicilio(models.Model):
    cod_domicilio = models.AutoField(primary_key=True)
    nombre_calle = models.CharField(max_length=200,blank= True)
    numero_calle = models.BigIntegerField(blank= True)
    nombre_barrio = models.CharField(max_length=200,blank= True)
    zona = models.OneToOneField(ZonaDomicilio, on_delete=models.CASCADE)



class Persona(models.Model):
    cuil = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200, blank= True)
    apellido = models.CharField(max_length=200, blank= True)
    fecha_nacimiento = models.DateField(blank= True)
    email = models.CharField(max_length=300,blank= True)
    domicilio = models.OneToOneField(Domicilio, on_delete=models.CASCADE)


class cadete(Persona):
    
    fecha_vigencia_carnet = models.DateField(blank=True)
    numero_patente = models.CharField(max_length=7,blank=True)
    fecha_ingreso = models.DateField(blank=True)

""" 

class Usuario(Persona):
    #nombreusuario = models.CharsFiled(max_length=300)
    #contraseña = models.CharsField(max_length=300)
    #tal vez esto lo determine en admin con los roles
"""