from django import views
from django.urls import path
from django.urls.resolvers import URLPattern
from apps.Pedido.views import lista_pedidosadmin, menu_edit, menu_editado
from apps.Pedido.views import detalle_pedidoadmin, pedidoadmin_edit
from apps.Pedido.views import detalle_pedido
from apps.Pedido.views import pedido_edit
from apps.Pedido.views import CarritoPedidoCliente,agregar_plato_carrito, eliminar_plato_carrito, limpiar_carrito, listarCategoriaPlato,menu_delete,lista_menus,creacion_pedido,lista_pedidos_cadetes,lista_pedidos,menu_detalle,creacion_menu, procesar_compra, promociones, restar_plato_carrito


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
path('editarPlato/<int:pk>',menu_edit, name='menu_edit'),
path('editarMenu',menu_editado,name='menu_editado'),
path('edit/<int:pk>',pedido_edit, name='edit_pedido'),
path('view/<int:pk>',detalle_pedido, name='detalle_pedido'),
path('editarpedido/<int:pk>',pedidoadmin_edit, name='pedidoadmin_edit'),
path('viewpedido/<int:pk>',detalle_pedidoadmin, name='detalle_pedidoadmin'),
path('listapedidosadmin',lista_pedidosadmin, name="lista_pedidosadmin"),

#carrito
path('CarritoPedidoCliente',CarritoPedidoCliente, name='CarritoPedidoCliente'),
path('addplato/<int:pk>', agregar_plato_carrito, name='addplato'),
path('deleteplato/<int:pk>',eliminar_plato_carrito, name='delplato'),
path('subplato/<int:pk>',restar_plato_carrito, name='subplato'),
path('clear',limpiar_carrito, name='cls'),
path('compra',procesar_compra, name='procesarcompra'),

]