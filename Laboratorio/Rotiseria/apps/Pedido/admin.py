from django.contrib import admin
from apps.Pedido.models import Pedido, Plato,EstadoEntrega,TipoPlato,Especialidad,ModalidadEntrega

# Register your models here.
admin.site.register(EstadoEntrega)
admin.site.register(Pedido)
admin.site.register(Plato)
admin.site.register(TipoPlato)
admin.site.register(Especialidad)
admin.site.register(ModalidadEntrega)