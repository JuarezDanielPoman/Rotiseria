from tkinter import Menu
from django import forms
from .models import Especialidad, ModalidadEntrega, Pedido
from .models import Plato
from django import forms


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ('codigo_plato','nombre_plato','precio_plato','vigencia_plato','estado_promocion','tipo_plato','especialidad')
        prefix = 'menu'
        widgets ={
        'nombre_plato': forms.TextInput(attrs={'name':"nombre_plato" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"nombre form-control mb-2 text-center" , 'id':"nombre_plato", 'placeholder':"Ingrese nombre del plato"}),
        'precio_plato': forms.NumberInput(attrs={'name':"precio_plato" , 'type':"number" , 'class':"form-control mb-2 text-center" , 'id':"precio_plato", 'placeholder':"Ingrese precio del plato"}),
        'tipo_plato': forms.Select(attrs={'name':"descripcion_zona"  , 'type':"text" , 'class':"nombre form-control mb-2 text-center" , 'id':"tipo_plato"}),
        'especialidad': forms.Select(attrs={'name':"especialidad"  , 'type':"text" , 'class':"nombre form-control mb-2 text-center" , 'id':"especialidad"}),
        }

        

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('persona','hora_entrega_hasta','estado_entrega','platos','modo_entrega')
        prefix = 'pedido'
        widgets = {
        'persona': forms.Select(attrs={'value':"pedido.persona"}),
        'hora_entrega_hasta': forms.TimeInput(attrs={'value':"pedido.hora_entrega_hasta"}),
        'estado_entrega': forms.Select(attrs={'value':"pedido.estado_entrega"}),
        'modo_entrega': forms.Select(attrs={'value':"pedido.modo_entrega"}),

        }

class PedidoCadeteForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('estado_entrega',)
        prefix = 'pedido'
        widgets = {
        }

        
class PedidoAdminForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('hora_entrega_hasta',)
        prefix = 'pedido'
        widgets = {
        }