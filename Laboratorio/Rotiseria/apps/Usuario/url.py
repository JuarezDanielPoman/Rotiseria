"""from django.conf.urls import url"""
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import creacion_cliente, persona_detalle

app_name='Usuario'

urlpatterns=[
    path('RegistroDeClientes',creacion_cliente,name='RegistroDeClientes'),
    path('Usuario/detalle.html',persona_detalle,name='detalle'),

]