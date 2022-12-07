from django import forms
from django.contrib import admin

from apps.Usuario.models import Domicilio, Persona, Telefono, ZonaDomicilio, Cadete

# Register your models here.
admin.site.register(Persona)
admin.site.register(Domicilio)
admin.site.register(ZonaDomicilio)
admin.site.register(Cadete)
admin.site.register(Telefono)


       