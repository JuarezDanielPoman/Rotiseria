from django.contrib import admin

from apps.Usuario.models import Domicilio, Persona, ZonaDomicilio, cadete

# Register your models here.
admin.site.register(Persona)
admin.site.register(Domicilio)
admin.site.register(ZonaDomicilio)
admin.site.register(cadete)