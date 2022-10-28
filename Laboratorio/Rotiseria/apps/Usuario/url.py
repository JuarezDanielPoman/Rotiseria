"""from django.conf.urls import url"""
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import creacion_cadete,persona_edit, creacion_cliente, persona_delete, persona_detalle

app_name='Usuario'

urlpatterns=[
    path('RegistroDeClientes',creacion_cliente,name='RegistroDeClientes'),
    path('RegistroDeCadetes',creacion_cadete,name='RegistroDeCadetes'),
    path('<int:pk>/', persona_detalle, name='persona_detalle'),
    path('', persona_delete, name='persona_delete'),
    path('edit/<int:pk>', persona_edit, name='persona_edit'),

]