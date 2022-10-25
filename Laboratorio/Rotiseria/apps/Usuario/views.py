from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from apps.Usuario.models import Persona
from apps.Usuario.forms import ZonaDomicilioForm
from apps.Usuario.forms import PersonaForm
from apps.Usuario.forms import DomicilioForm
from apps.Usuario.forms import TelefonoForm




# Create your views here.
id=0
def creacion_cliente(request):
    if (request.method == 'POST'):
        domicilio_form = DomicilioForm(request.POST, prefix='domicilio')
        persona_form = PersonaForm(request.POST, prefix='persona')
        telefono_form = TelefonoForm(request.POST, prefix='telefono')
        zona_form = ZonaDomicilioForm(request.POST, prefix='zona')
        if domicilio_form.is_valid() and persona_form.is_valid() and telefono_form.is_valid() and zona_form.is_valid():
            p=persona_form.save(commit=False)
            d=domicilio_form.save(commit=False)
            t=telefono_form.save(commit=False)
            z=zona_form.save(commit=False)
            t.save()
            z.save()

            d.zona_id=z.cod_zona
            d.save()

            p.domicilio_id=d.cod_domicilio
            p.telefono_id=t.id
            p.save()

            print(request.post['persona'])
            messages.success(request,
            'Se ha agregado correctamente la persona {}'.format(p,d,t,z))
            return redirect(reverse('Usuario:detalle', args={p.id}))
    else:
        domicilio_form = DomicilioForm(prefix='domicilio')
        persona_form = PersonaForm(prefix='persona')
        telefono_form = TelefonoForm(prefix='telefono')
        zona_form = ZonaDomicilioForm(prefix='zona')
    return render(request,'Usuario/RegistroDeClientes.html',{'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form,'zona_form': zona_form})
 


def persona_detalle(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request,
                  'Usuario/detalle.html',
                  {'persona': persona})
