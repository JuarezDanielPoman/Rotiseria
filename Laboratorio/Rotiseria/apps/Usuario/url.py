"""from django.conf.urls import url"""
from django import views
from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from .views import creacion_cadete, editar_cadete,persona_delete_lista,cadete_delete,logout_view,buscar_cadetes,login_view, buscar_personas,lista_cadetes,lista_personas,persona_edit, creacion_cliente, persona_delete, persona_detalle, registrarUsuario
from django.contrib.auth.views import LoginView
app_name='Usuario'

urlpatterns=[
    path('lista-clientes', lista_personas, name='lista_de_personas'),
    path('registrar-clientes',creacion_cliente,name='RegistroDeClientes'),
    path('editar-cliente/<int:pk>', persona_edit, name='persona_edit'),

    path('lista-empleados', lista_cadetes, name='lista_de_cadetes'),
    path('registrar-empleado',creacion_cadete,name='RegistroDeCadetes'),
    path('editar-empleado/<int:pk>',editar_cadete,name='editar_cadete'),


    path('detalle/<int:pk>/', persona_detalle, name='persona_detalle'),
    path('', persona_delete, name='persona_delete'),
    
    
    path('buscarCadete/', buscar_personas, name='buscar_personas'),
    path('buscarPersona/', buscar_cadetes, name='buscar_cadetes'),
    path('login', login_view, name='login'),
    path("logout", logout_view, name="logout"),
    path('delete/', cadete_delete, name='cadete_delete'),
    path('deletepersona/', persona_delete_lista, name='persona_delete_lista'),
    path('CrearUsuario', registrarUsuario, name='registrar')

]