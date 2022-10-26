
from tkinter import Menu
from django import forms

from apps.Pedido.models import Plato


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ('codigo_plato','nombre_plato','precio_plato','vigencia_plato','estado_promocion','tipo_plato','especialidad')
        prefix = 'menu'