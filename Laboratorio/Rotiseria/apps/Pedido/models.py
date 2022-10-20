from email.policy import default
from enum import unique
from random import choices
from django.db import models
from apps.Usuario.models import Persona
from tkinter import CASCADE
from cgitb import text

# Create your models here.
class EstadoEntrega(models.Model):
    estado_entrega = models.AutoField(primary_key=True)
    descripcion_estado = models.CharField(max_length=200,blank=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.descripcion_estado)

class TipoPlato(models.Model):
    tipo_plato = models.AutoField(primary_key=True)
    descripcion_tipo_plato = models.CharField(max_length=100,blank=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.descripcion_tipo_plato)

class Especialidad(models.Model):
    especialidad = models.AutoField(primary_key=True)
    descripcion_especialidad = models.CharField(max_length=200,blank=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.descripcion_especialidad)

class Plato(models.Model):
    codigo_plato = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=200,blank=True)
    tipo_plato = models.OneToOneField(TipoPlato,on_delete=models.CASCADE)
    especialidad = models.OneToOneField(Especialidad,on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} - {1} - {2} - {3}"
        return texto.format(self.codigo_plato, self.nombre_plato, self.tipo_plato, self.especialidad)

class ModalidadEntrega(models.Model):
    modoentrega = models.AutoField(primary_key=True)
    descripcion_modo_entrega = models.CharField(max_length=200,blank=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.descripcion_modo_entrega)

class Pedido(models.Model):
    cod_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    persona = models.ForeignKey(Persona,blank=False,null=False,on_delete=models.CASCADE)
    hora_entrega_desde = models.TimeField(blank= True)
    hora_entrega_hasta = models.TimeField(blank= True)
    estado_entrega = models.OneToOneField(EstadoEntrega, on_delete=models.CASCADE)
    platos = models.ManyToManyField(Plato)
    modo_entrega = models.OneToOneField(ModalidadEntrega,on_delete=models.CASCADE)


    def __str__(self):
        texto = "{0} - {1} - {2} - {3}"
        return texto.format(self.cod_pedido, self.fecha_pedido, self.persona, self.hora_entrega_desde, self.hora_entrega_hasta, self.estado_entrega, self.platos, self.modo_entrega)

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
   
    opcion = [
        ('Envio','envio'),
        ('Retiro','retiro'),

    ]
    modalidadentrega = models.CharField(max_length=100,blank= True,choices=opcion)
    
     
    especialidadades = [
        ('Normal','normal'),
        ('Vegetariano','vegetariano'),
        ('celiaco','Celiaco'),
        ('diabetico','Diabetico'),

    ]
    especialidad = models.CharField(max_length=100,blank= True,choices=especialidadades)
    
    tipo_platos = [
        ('Entrada','entrada'),
        ('Plato Principal','plato Principal'),
        ('postre','Postre')
    ]
    tipo_plato = models.CharField(max_length=100,blank= True,choices=tipo_platos)
    
    """