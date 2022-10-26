from django import views
from django.urls import path
from django.urls.resolvers import URLPattern

from apps.Pedido.views import creacion_menu, promociones


app_name='Pedido'

urlpatterns=[
path('RegistroDeMenu',creacion_menu,name='RegistroDeClientes'),
path('promociones',promociones, name="promociones")
]