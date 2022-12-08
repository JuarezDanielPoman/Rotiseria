from django import views
from django.urls import path
from django.urls.resolvers import URLPattern
from apps.Pedido.views import *

app_name='Pedido'

urlpatterns=[
path('promociones',promociones, name="promociones"),
path('categoria',listarCategoriaPlato,name="categorias"),

#PLATOS
path('listado-platos',lista_menus, name="listademenus"),
path('registrar-plato',creacion_menu,name='RegistroDeMenu'),
path('editar-plato/<int:pk>',menu_edit, name='menu_edit'),
path('detalle-plato/<int:pk>', menu_detalle, name='menu_detalle'),
path('eliminar-plato/',menu_delete, name="menu_delete"),

#PEDIDOS
path('listado-pedidos',lista_pedidosadmin, name="lista_pedidosadmin"),
path('registrar-pedido',creacion_pedido, name='RegistroDePedido'),
path('editar-pedido/<int:pk>',pedidoadmin_edit, name='pedidoadmin_edit'),
path('detalle-pedido/<int:pk>',detalle_pedidoadmin, name='detalle_pedidoadmin'),
path('mis-pedidos',lista_pedidosrealizados, name="listapedidosrealizados"),

path('pedidos-asignados',lista_pedidos_asignados, name="lista_pedidos_asignados"),
path('pedidos-realizados',pedidos_realizados_cadete, name="pedidos_realizados_cadete"),
path('lista-pedidos-disponibles',lista_pedidosdisponibles, name="lista_pedidosdisponibles"),


path('edit/<int:pk>',pedido_edit, name='edit_pedido'),
path('VistaPedido/<int:pk>',detalle_pedido, name='detalle_pedido'),


path('buscar/',buscar_platos, name="buscar_platos"),
path('buscarpedido/',buscar_pedidos, name="buscar_pedidos"),
path('buscarplatoadmin/',buscar_platosadmin, name="buscar_platosadmin"),




#CARRITO
path('CarritoPedidoCliente',CarritoPedidoCliente, name='CarritoPedidoCliente'),
path('addplato/<int:pk>', agregar_plato_carrito, name='addplato'),
path('deleteplato/<int:pk>',eliminar_plato_carrito, name='delplato'),
path('subplato/<int:pk>',restar_plato_carrito, name='subplato'),
path('clear',limpiar_carrito, name='cls'),
path('compra',procesar_compra, name='procesarcompra'),

]