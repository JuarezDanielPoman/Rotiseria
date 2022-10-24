from ast import pattern
import email
from email.policy import default
from re import A
from tkinter import Widget
from xml.dom.minidom import AttributeList
from django import forms
from django.core.exceptions import ValidationError
from django.forms import NumberInput, TextInput
from .models import Domicilio, Persona,Telefono,ZonaDomicilio

class DomicilioForm(forms.ModelForm):
    cuil = forms.CharField(widget=forms.TextInput(attrs={'name':"cuil" ,'required':True, 'type':"number" , 'class':"form-control mb-2 text-center" , 'id':"cuil", 'placeholder':"Ingrese su Cuil"}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'name':"nombre" ,'required':True,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"nombre form-control mb-2 text-center" , 'id':"nombre", 'placeholder':"Ingrese su Nombre"}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'name':"apellido" ,'required':True,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"form-control mb-2 text-center" , 'id':"apellidoi", 'placeholder':"Ingrese su Apellido"}))
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class':"form-control mb-2",'required':True ,'type':"date" ,'id':"fechanacimiento"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':"form-control mb-2 text-center" ,'required':True, 'type':"email", 'id':"correo",'placeholder':"Ingrese su Mail"}),)
    telefono = forms.CharField()
    descripcion_zona = forms.CharField()    
    class Meta:
        model = Domicilio
        fields = ('cuil', 'apellido','nombre', 'fecha_nacimiento', 'email','numero_calle','nombre_calle','nombre_barrio','descripcion_zona')


"""

class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ('cuil', 'apellido','nombre', 'fecha_nacimiento', 'email','domicilio','telefono')
    
        widgets = {
            'cuil': forms.NumberInput(attrs={'name':"cuil" , 'type':"number" , 'class':"form-control mb-2 text-center" , 'id':"cuil", 'placeholder':"Ingrese su Cuil"}),
            'nombre': forms.TextInput(attrs={'name':"nombre" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"nombre form-control mb-2 text-center" , 'id':"nombre", 'placeholder':"Ingrese su Nombre"}),
            'apellido': forms.TextInput(attrs={'name':"apellido" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"form-control mb-2 text-center" , 'id':"apellidoi", 'placeholder':"Ingrese su Apellido"}),
            'email': forms.EmailInput(attrs={'class':"form-control mb-2 text-center" , 'type':"email", 'id':"correo",'placeholder':"Ingrese su Mail"}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':"form-control mb-2" ,'type':"date" ,'id':"fechanacimiento"})
        }

        """

class Telefono(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ('tipo_telefono','numero')






    """
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            instance=self.instance
            if instance.pk:
                if Persona.objects.filter(domicilio=instance).exists():
                    self.initial['domicilio'] = Persona.objects.get(domicilio=instance)
    """   
"""
from django.forms.models import inlineformset_factory
ChildFormset = inlineformset_factory(
    Domicilio,Persona , fields=('domicilio',)
)
"""