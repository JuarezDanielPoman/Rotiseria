from cgitb import text
from email.policy import default
from enum import unique
from random import choices
from re import S
from secrets import choice
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class ZonaDomicilio(models.Model):
    cod_zona = models.AutoField(primary_key=True)
    descripcion_zona = models.CharField(max_length=200,blank= True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.descripcion_zona)


class Domicilio(models.Model):
    cod_domicilio = models.AutoField(primary_key=True)
    nombre_calle = models.CharField(max_length=200,blank= True)
    numero_calle = models.BigIntegerField(blank= True)
    nombre_barrio = models.CharField(max_length=200,blank= True)
    zona = models.OneToOneField(ZonaDomicilio, on_delete=models.CASCADE)

    def __str__(self):
        texto = "Barrio: {0} - Calle: {1} - Número: {2} - Zona: {3}"
        return texto.format(self.nombre_barrio, self.nombre_calle,self.numero_calle,self.zona)

class Telefono(models.Model):
    telefono_op=[('fijo','Fijo'), ('celular','Celular')]
    tipo_telefono = models.CharField(max_length=10, choices=telefono_op)
    numero = models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        texto = "{0} / {1}"
        return texto.format(self.numero,self.tipo_telefono)

class Persona(models.Model):
    cuil = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=200, blank= True)
    apellido = models.CharField(max_length=200, blank= True)
    fecha_nacimiento = models.DateField(blank= True)
    email = models.CharField(max_length=300,blank= True)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, default=None)
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True,unique=True)

    def __str__(self):
        texto = "{0} - {1} - {2} - {3} - {4} - {5}"
        return texto.format(self.cuil, self.apellido, self.nombre, self.fecha_nacimiento, self.domicilio, self.email)


class cadete(Persona):
    #persona = models.ForeignKey(Persona, on_delete=models.CASCADE,default=None)
    fecha_vigencia_carnet = models.DateField(blank=True)
    numero_patente = models.CharField(max_length=7,blank=True)
    fecha_ingreso = models.DateField(blank=True)

    def __str__(self):
        texto = "{0} - Ingreso laboral: {1} - Vigencia carnet: {2} - Patente: {3} - Zona: {4}"
        return texto.format(self.cuil, self.fecha_ingreso, self.fecha_vigencia_carnet, self.numero_patente, self.domicilio.zona)


