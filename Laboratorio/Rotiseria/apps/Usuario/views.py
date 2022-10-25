from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from apps.Usuario.forms import ZonaDomicilioForm
from apps.Usuario.forms import PersonaForm
from apps.Usuario.forms import DomicilioForm
from apps.Usuario.forms import TelefonoForm




# Create your views here.

def creacion_cliente(request):
    if (request.method == 'POST'):
        domicilio_form = DomicilioForm(request.POST, prefix='domicilio')
        persona_form = PersonaForm(request.POST, prefix='persona')
        telefono_form = TelefonoForm(request.POST, prefix='telefono')
        zona_form = ZonaDomicilioForm(request.POST, prefix='zona')
        if domicilio_form.is_valid() and persona_form.is_valid() and telefono_form.is_valid() and zona_form.is_valid():
            p=persona_form.save(commit=True)
            d=domicilio_form.save(commit=True)
            t=telefono_form.save(commit=True)
            z=zona_form.save(commit=True)
            messages.success(request,
            'Se ha agregado correctamente la persona {}'.format(p,d,t,z))
        return redirect(reverse('Usuario:RegistroDeClientes'))
    else:
        domicilio_form = DomicilioForm(prefix='domicilio')
        persona_form = PersonaForm(prefix='persona')
        telefono_form = TelefonoForm(prefix='telefono')
        zona_form = ZonaDomicilioForm(prefix='zona')
        return render(request,'Usuario/RegistroDeClientes.html',{'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form,'zona_form': zona_form})
 

