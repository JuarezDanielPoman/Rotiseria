"""from django.conf.urls import url"""
from django import views
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import creacion_cadete,logout_view,buscar_cadetes,login_view, buscar_personas,lista_cadetes,lista_personas,persona_edit, creacion_cliente, persona_delete, persona_detalle

app_name='Usuario'

urlpatterns=[
    path('RegistroDeClientes',creacion_cliente,name='RegistroDeClientes'),
    path('RegistroDeCadetes',creacion_cadete,name='RegistroDeCadetes'),
    path('<int:pk>/', persona_detalle, name='persona_detalle'),
    path('', persona_delete, name='persona_delete'),
    path('edit/<int:pk>', persona_edit, name='persona_edit'),
    path('ListaDeCadetes', lista_cadetes, name='lista_de_cadetes'),
    path('ListaDePersonas', lista_personas, name='lista_de_personas'),
    path('buscar/', buscar_personas, name='buscar_personas'),
    path('buscar/', buscar_cadetes, name='buscar_cadetes'),
    path('login', login_view, name='login'), 
    path("logout", logout_view, name="logout")

]