from ast import pattern
import email
from re import A
from tkinter import Widget
from xml.dom.minidom import AttributeList
from django import forms
from django.core.exceptions import ValidationError
from django.forms import NumberInput, TextInput

from .models import Persona

class PersonaForm(forms.ModelForm):
    numero = forms.CharField()
    tipo_telefono = forms.CharField()
    class Meta:
        model = Persona
        fields = ('cuil', 'apellido','nombre', 'fecha_nacimiento', 'email','numero','domicilio')
    
        widgets = {
            'cuil': forms.NumberInput(attrs={'name':"cuil" , 'type':"number" , 'class':"form-control mb-2 text-center" , 'id':"cuil", 'placeholder':"Ingrese su Cuil"}),
            'nombre': forms.TextInput(attrs={'name':"nombre" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"nombre form-control mb-2 text-center" , 'id':"nombre", 'placeholder':"Ingrese su Nombre"}),
            'apellido': forms.TextInput(attrs={'name':"apellido" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"form-control mb-2 text-center" , 'id':"apellidoi", 'placeholder':"Ingrese su Apellido"}),
            'email': forms.EmailInput(attrs={'class':"form-control mb-2 text-center" , 'type':"email", 'id':"correo",'placeholder':"Ingrese su Mail"}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':"form-control mb-2" ,'type':"date" ,'id':"fechanacimiento"})

        }

        

"""
class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ('nombre', 'tipo_asistencias', 'requisitos', 'fecha_inicio', 'fecha_fin')

        widgets = {
            'requisitos': forms.ClearableFileInput(),
            'fecha_inicio': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_fin': DateInput(format='%y-%m-%d', attrs={'type': 'date'})
        }

    def clean_requisitos(self):
        requisitos = self.cleaned_data['requisitos']
        if requisitos:
            extension = requisitos.name.rsplit('.', 1)[1].lower()
            if extension != 'pdf':
                raise ValidationError('El archivo seleccionado no tiene el formato PDF.')
        return requisitos

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = self.cleaned_data['fecha_inicio']
        fecha_fin = self.cleaned_data['fecha_fin']
        # Verifica que la fecha de inicio sea anterior a fecha fin.
        if fecha_fin and fecha_inicio > fecha_fin:
            raise ValidationError(
                {'fecha_inicio': 'La Fecha de Inicio no puede ser posterior que la fecha fin'},
                code='invalido'
            )
        return cleaned_data
"""