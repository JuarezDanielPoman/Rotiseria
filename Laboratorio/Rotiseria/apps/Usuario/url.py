"""from django.conf.urls import url"""
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import creacion_cadete, creacion_cliente, persona_detalle

app_name='Usuario'

urlpatterns=[
    path('RegistroDeClientes',creacion_cliente,name='RegistroDeClientes'),
    path('RegistroDeCadetes',creacion_cadete,name='RegistroDeCadetes'),
    path('<int:pk>/', persona_detalle, name='persona_detalle'),

]