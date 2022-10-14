from django.db import models

# Create your models here.
class Pedido(models.Model):
    cod_pedido = models.IntegerField(unique=True)