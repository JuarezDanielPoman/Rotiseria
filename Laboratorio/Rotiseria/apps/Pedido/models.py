from random import choices
from django.db import models

# Create your models here.

class Pedidos(models.model):
    cod_pedido = models.AutoField(PrimaryKey=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    #usuario = models.ForeignKey(Usuario,blank=False,null=False,on_delete=models.CASCADE)
    opcion = [
        ('Envio','envio'),
        ('Retiro','retiro'),

    ]
    modalidadentrega = models.CharField(choices=opcion)
    hora_entrega_desde = models.DateTimeField()
    estados = [
        ('Pendiente','pendiente'),
        ('En preparacion','en preparacion'),
        ('En camino','en camino'),
        ('Entregado','entregado'),
        ('Devuelto','devuelto'),
        ('Cancelado','cancelado'),

    ]
    estado_entrega = models.CharField(choices=estados)
    hora_entrega_hasta = models.DateTimeField()

class platos(models.model):
    codigo_plato = models.AutoField(PrimaryKey=True)
    tipo_platos = [
        ('Entrada','entrada'),
        ('Plato Principal','plato Principal','principal')
        ('postre','Postre')
    ]
    tipo_plato = models.CharField(choices=tipo_platos)
    especialidadades = [
        ('Normal','normal'),
        ('Vegetariano','vegetariano')
        ('celiaco','Celiaco')
        ('diabetico','Diabetico')

    ]
    especialidad = models.CharField(choices=especialidadades)
    pedido = models.ManyToManyField(Pedidos)