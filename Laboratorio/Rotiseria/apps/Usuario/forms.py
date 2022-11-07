
from dataclasses import field
import email
from email.policy import default
from multiprocessing import context
from pyexpat import model
from re import A
from tkinter import Widget
from xml.dom.minidom import AttributeList
from django import forms
from django.core.exceptions import ValidationError
from django.forms import NumberInput, TextInput
from .models import Domicilio, Persona,Telefono,ZonaDomicilio,cadete
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DomicilioForm(forms.ModelForm):   
    class Meta:
        model = Domicilio
        fields = ('numero_calle','nombre_calle','nombre_barrio')
        prefix = 'domicilio'

        widgets = {
        'numero_calle': forms.NumberInput(attrs={'name':"numero_calle" , 'type':"number" , 'class':"form-control mb-2 text-center" , 'id':"numero_calle", 'placeholder':"Ingrese numero de calle"}),
        'nombre_calle': forms.TextInput(attrs={'name':"nombre_calle" , 'type':"text" , 'class':"form-control mb-2 text-center" , 'id':"nombre_calle", 'placeholder':"Ingrese nombre de calle"}),
        'nombre_barrio': forms.TextInput(attrs={'name':"nombre_barrio" , 'type':"text" , 'class':"form-control mb-2 text-center" , 'id':"nombre_barrio", 'placeholder':"Ingrese nombre de barrio"}),

        }


class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ('cuil', 'apellido','nombre', 'fecha_nacimiento', 'email')
        prefix = 'persona'

        widgets = {
            'cuil': forms.NumberInput(attrs={'name':"cuil" , 'type':"number" , 'class':"form-control mb-2 text-center" , 'id':"cuil", 'placeholder':"Ingrese su Cuil"}),
            'nombre': forms.TextInput(attrs={'name':"nombre" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"nombre form-control mb-2 text-center" , 'id':"nombre", 'placeholder':"Ingrese su Nombre"}),
            'apellido': forms.TextInput(attrs={'name':"apellido" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"form-control mb-2 text-center" , 'id':"apellidoi", 'placeholder':"Ingrese su Apellido"}),
            'email': forms.EmailInput(attrs={'class':"form-control mb-2 text-center" , 'type':"email", 'id':"correo",'placeholder':"Ingrese su Mail"}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':"form-control mb-2" ,'type':"date" ,'id':"fechanacimiento"})
        }

        

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ('tipo_telefono','numero')
        prefix = 'telefono'
        widgets = {
            'numero': forms.NumberInput(attrs={'name':"numero" , 'type':"number" , 'class':"form-control mb-2 text-center" , 'id':"numero", 'placeholder':"Ingrese su numero de telefono"}),
            'tipo_telefono': forms.Select(attrs={'name':"tipo_telefono" , 'type':"number" , 'class':"form-control mb-2 text-center" , 'id':"tipo_telefono"}),
        }

class ZonaDomicilioForm(forms.ModelForm):
    class Meta:
        model = ZonaDomicilio
        fields = ('descripcion_zona',)
        prefix = 'zona'
        op=[('norte','Norte'),('sur','Sur'),('este','Este'),('oeste','Oeste')]
        widgets = {
        'descripcion_zona': forms.Select(choices=op,attrs={'name':"descripcion_zona"  , 'type':"text" , 'class':"nombre form-control mb-2 text-center" , 'id':"descripcion_zona", 'placeholder':"Ingrese la zona"}),
        }



class CadeteForm(forms.ModelForm):
    
    class Meta:
        model = cadete
        fields = ('user','cuil', 'apellido','nombre', 'fecha_nacimiento', 'email','fecha_vigencia_carnet','numero_patente','fecha_ingreso')
        prefix = 'persona'

        widgets = {
            'cuil': forms.NumberInput(attrs={'name':"cuil" , 'type':"number" , 'class':"form-control mb-2 text-center" , 'id':"cuil", 'placeholder':"Ingrese su Cuil"}),
            'nombre': forms.TextInput(attrs={'name':"nombre" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"nombre form-control mb-2 text-center" , 'id':"nombre", 'placeholder':"Ingrese su Nombre"}),
            'apellido': forms.TextInput(attrs={'name':"apellido" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"form-control mb-2 text-center" , 'id':"apellidoi", 'placeholder':"Ingrese su Apellido"}),
            'email': forms.EmailInput(attrs={'class':"form-control mb-2 text-center" , 'type':"email", 'id':"correo",'placeholder':"Ingrese su Mail"}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':"form-control mb-2" ,'type':"date" ,'id':"fechanacimiento"}),
            'numero_patente': forms.TextInput(attrs={'name':"numero_patente" ,'pattern':"[a-zA-ZñÑáéíóúÁÉÍÓÚüÜ ']{2,25}" , 'type':"text" , 'class':"form-control mb-2 text-center" , 'id':"numero_patente", 'placeholder':"Ingrese su Patente"}),
            'fecha_vigencia_carnet': forms.DateInput(attrs={'class':"form-control mb-2" ,'type':"date" ,'id':"fecha_vigencia_carnet"}),
            'fecha_ingreso': forms.DateInput(attrs={'class':"form-control mb-2" ,'type':"date" ,'id':"fecha_ingreso"})

        }

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password','required': 'required'}, ))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password','required': 'required'}, ))
    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email","password1","password2"]

        widgets = {
            'username': forms.TextInput(attrs={'name':"username" , 'type':"text" , 'class':"form-control mb-2 text-center" , 'id':"username", 'placeholder':"Ingrese nombre de usuario"}),

        }


