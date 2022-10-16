from django.db import models

# Create your models here.

class Persona(models.model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_legth=300)
    #falta domicilio y telefono
    
class cadete(Persona):
    vigenciadelcarnet = models.DateField()
    numero_patente = models.CharField()
    fecha_ingreso = models.DateField()

"""
class Usuario(Persona):
    #nombreusuario = models.CharsFiled(max_length=300)
    #contraseña = models.CharsField(max_length=300)
    #tal vez esto lo determine en admin con los roles
"""