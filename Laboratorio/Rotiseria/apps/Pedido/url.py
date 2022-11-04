from django import views
from django.urls import path
from django.urls.resolvers import URLPattern
from apps.Pedido.views import CarritoPedidoCliente,agregar_plato_carrito, eliminar_plato_carrito, limpiar_carrito, listarCategoriaPlato,menu_delete,lista_menus,creacion_pedido,lista_pedidos_cadetes,lista_pedidos,menu_detalle,creacion_menu, menu_edit, menu_editado, procesar_compra, promociones, restar_plato_carrito


app_name='Pedido'

urlpatterns=[
path('categoria',listarCategoriaPlato,name="categorias"),
path('RegistroDeMenu',creacion_menu,name='RegistroDeMenu'),
path('promociones',promociones, name="promociones"),
path('<int:pk>/', menu_detalle, name='menu_detalle'),
path('RegistroDePedido/',creacion_pedido, name='RegistroDePedido'),
path('ListaDepedidos',lista_pedidos, name="ListaDepedidos"),
path('listapedidoscadetes',lista_pedidos_cadetes, name="listapedidoscadetes"),
path('listademenus',lista_menus, name="listademenus"),
path('delete/',menu_delete, name="menu_delete"),
path('editarMenu/<int:pk>',menu_edit, name='editar_menu'),
path('EditarPlato',menu_editado, name="editando_menu"),

#carrito
path('CarritoPedidoCliente',CarritoPedidoCliente, name='CarritoPedidoCliente'),
path('addplato/<int:pk>', agregar_plato_carrito, name='addplato'),
path('deleteplato/<int:pk>',eliminar_plato_carrito, name='delplato'),
path('subplato/<int:pk>',restar_plato_carrito, name='subplato'),
path('clear',limpiar_carrito, name='cls'),
path('compra',procesar_compra, name='procesarcompra'),
]