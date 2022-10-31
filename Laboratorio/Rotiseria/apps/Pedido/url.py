from django import views
from django.urls import path
from django.urls.resolvers import URLPattern
from apps.Pedido.views import lista_menus,creacion_pedido,lista_pedidos_cadetes,lista_pedidos,RegistroPedidoCliente,menu_detalle,creacion_menu, promociones


app_name='Pedido'

urlpatterns=[
path('RegistroDeMenu',creacion_menu,name='RegistroDeMenu'),
path('RegistroPedidoCliente/',RegistroPedidoCliente, name='RegistroPedidoCliente'),
path('promociones',promociones, name="promociones"),
path('<int:pk>/', menu_detalle, name='menu_detalle'),
path('RegistroDePedido/',creacion_pedido, name='RegistroDePedido'),
path('ListaDepedidos',lista_pedidos, name="ListaDepedidos"),
path('listapedidoscadetes',lista_pedidos_cadetes, name="listapedidoscadetes"),
path('listademenus',lista_menus, name="listademenus"),

]