from email.policy import default
from enum import unique
from random import choices
from django.db import models
from apps.Usuario.models import Persona
from tkinter import CASCADE

# Create your models here.
class EstadoEntrega(models.Model):
    estado_entrega = models.CharField(max_length=1,blank=True,unique=True)
    descripcion_estado = models.CharField(max_length=200,blank=True)

class Plato(models.Model):
    codigo_plato = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=200,blank=True)
    tipo_platos = [
        ('Entrada','entrada'),
        ('Plato Principal','plato Principal'),
        ('postre','Postre')
    ]
    tipo_plato = models.CharField(max_length=100,blank= True,choices=tipo_platos)
    especialidadades = [
        ('Normal','normal'),
        ('Vegetariano','vegetariano'),
        ('celiaco','Celiaco'),
        ('diabetico','Diabetico'),

    ]
    especialidad = models.CharField(max_length=100,blank= True,choices=especialidadades)


class Pedido(models.Model):
    cod_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    persona = models.ForeignKey(Persona,blank=False,null=False,on_delete=models.CASCADE)
    opcion = [
        ('Envio','envio'),
        ('Retiro','retiro'),

    ]
    modalidadentrega = models.CharField(max_length=100,blank= True,choices=opcion)
    hora_entrega_desde = models.TimeField(blank= True)
    hora_entrega_hasta = models.TimeField(blank= True)
    estado_entrega = models.OneToOneField(EstadoEntrega, on_delete=models.CASCADE)
    platos = models.ManyToManyField(Plato)


"""
    estados = [
        ('Pendiente','pendiente'),
        ('En preparacion','en preparacion'),
        ('En camino','en camino'),
        ('Entregado','entregado'),
        ('Devuelto','devuelto'),
        ('Cancelado','cancelado'),

    ]
    estado_entrega = models.CharField(choices=estados,default='Pendiente')
    """