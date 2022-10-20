from django.contrib import admin
from apps.Pedido.models import Pedido, Plato,EstadoEntrega

# Register your models here.
admin.site.register(EstadoEntrega)
admin.site.register(Pedido)
admin.site.register(Plato)