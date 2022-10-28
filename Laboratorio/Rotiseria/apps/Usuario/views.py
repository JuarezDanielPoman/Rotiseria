from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from apps.Usuario.forms import CadeteForm
from apps.Usuario.models import Persona, cadete
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

            messages.success(request,
            'Se ha agregado correctamente la persona {}'.format(p.id))
            return redirect(reverse('Usuario:persona_detalle', args={p.id}))
    else:
        domicilio_form = DomicilioForm(prefix='domicilio')
        persona_form = PersonaForm(prefix='persona')
        telefono_form = TelefonoForm(prefix='telefono')
        zona_form = ZonaDomicilioForm(prefix='zona')
    return render(request,'Usuario/RegistroDeClientes.html',{'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form,'zona_form': zona_form})

def creacion_cadete(request):
    if (request.method == 'POST'):
        domicilio_form = DomicilioForm(request.POST, prefix='domicilio')
        persona_form = CadeteForm(request.POST, prefix='persona')
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
        persona_form = CadeteForm(prefix='persona')
        telefono_form = TelefonoForm(prefix='telefono')
        zona_form = ZonaDomicilioForm(prefix='zona')
    return render(request,'Usuario/RegistroDeCadetes.html',{'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form,'zona_form': zona_form})

def persona_detalle(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request,
                  'Usuario/detalle.html',
                  {'persona': persona})

def persona_delete(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            persona = get_object_or_404(Persona, pk=request.POST['id'])
            print(persona)
            persona.delete()
            messages.success(request,
            'Se ha eliminado la persona {}'.format(persona))
    return render(request,
                  'Usuario/detalle.html')

def persona_edit(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        domicilio_form = DomicilioForm(request.POST, prefix='domicilio')
        persona_form = CadeteForm(request.POST, prefix='persona',instance=persona)
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

            messages.success(request,
            'Se ha agregado correctamente la persona {}'.format(p,d,t,z))
            return redirect(reverse('Usuario:persona_detalle', args={p.id}))
    else:
        domicilio_form = DomicilioForm(prefix='domicilio')
        persona_form = PersonaForm(prefix='persona')
        telefono_form = TelefonoForm(prefix='telefono')
        zona_form = ZonaDomicilioForm(prefix='zona')
    return render(request,'Usuario/persona_edit.html',{'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form,'zona_form': zona_form})

def lista_cadetes(request):
    listaCadetes = cadete.objects.all()
    return render(request,'Usuario/ListaDeCadetes.html',{'cadetes': listaCadetes})

