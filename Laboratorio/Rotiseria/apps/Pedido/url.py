from django import views
from django.urls import path
from django.urls.resolvers import URLPattern

from apps.Pedido.views import RegistroPedidoCliente, creacion_menu, promociones


app_name='Pedido'

urlpatterns=[
path('RegistroDeMenu',creacion_menu,name='RegistroDeClientes'),
path('promociones',promociones, name="promociones"),
path('RegistroPedidoCliente/',RegistroPedidoCliente, name='RegistroPedidoCliente')
]