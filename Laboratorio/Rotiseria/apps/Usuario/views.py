from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from apps.Usuario.models import Persona

from apps.Usuario.models import Domicilio


from .forms import PersonaForm

# Create your views here.

def creacion_cliente(request):
    if (request.method == 'POST'):
        cliente_form = PersonaForm(request.POST)
        if cliente_form.is_valid():
            nuevo_cliente = cliente_form.save(commit=False)
            nuevo_cliente.save()
            
    else:
        cliente_form = PersonaForm()    
    return render(request,'Usuario/RegistroDeClientes.html',{'form': cliente_form})
 