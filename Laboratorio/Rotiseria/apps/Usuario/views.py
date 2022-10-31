from urllib import request
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from apps.Usuario.forms import CadeteForm, CustomUserCreationForm
from apps.Usuario.models import Persona, cadete
from apps.Usuario.forms import ZonaDomicilioForm
from apps.Usuario.forms import PersonaForm
from apps.Usuario.forms import DomicilioForm
from apps.Usuario.forms import TelefonoForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import *
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout




# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse('Usuario:logout'))
        messages.error(request, 'Usuario y/o contraseña incorrecta')
        #return render(request,'base/home.html')
    
    return render(request, 'base/home.html')

def registrarUsuario(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect('base/home.html')
        else:
            data['form'] = formulario
    return render(request,'Usuario/CrearUsuario.html',data)


def logout_view(request):
    logout(request) 
    return render(request, 'base/home.html')

def login_view(request):
    if request.method == "POST":   
        try:
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
        except MultiValueDictKeyError:
            username = 'Error'
            password = 'Error'
        user = authenticate(request, username=username, password=password)
        if user: 
            login(request, user)
            messages.success(request, 'Bienvenido, {user.username}')
            return render(request, 'base/home.html')
            #return HttpResponseRedirect(reverse('baseCadete'))
        else:
            messages.error(request, 'Usuario y/o contraseña incorrecta')
            return render(request, 'base/home.html')
    return render(request, 'base/home.html')

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
            persona.delete()
            messages.success(request,
            'Se ha eliminado la persona {}'.format(persona))
    return render(request,
                  'Usuario/detalle.html')

def persona_edit(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        domicilio_form = DomicilioForm(request.POST, prefix='domicilio')
        persona_form = PersonaForm(request.POST, prefix='persona',instance=persona)
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


def lista_personas(request):
    listaPersonas = Persona.objects.all()
    return render(request,'Usuario/ListaDePersonas.html',{'personas': listaPersonas})


# def buscar_personas(request):
#     if request.method == 'GET':
#         nombrebuscado = request.GET.get('buscar',)
#         buscar_persona=Persona.objects.filter(apellido=nombrebuscado)
#         print(nombrebuscado)
#         print(buscar_persona)
#         return render(request,'Usuario/ListaDePersonas.html',{'personas':buscar_persona})

def buscar_personas(request):
    programas = Persona.objects.all()

    if 'buscar' in request.GET:
        buscar_persona = programas.filter(nombre__icontains=request.GET['buscar'])
    print(request.GET['buscar'])
    return render(request, 'Usuario/ListaDePersonas.html',
                  {'personas': buscar_persona})

def buscar_cadetes(request):
    busqueda = request.POST.get("buscar")
    product_list = cadete.objects.order_by('nombre')
    page = request.GET.get('page', 1)

    if busqueda:
        product_list = cadete.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    
    try:
        paginator = Paginator(product_list, 12)
        product_list = paginator.page(page)
    except:
        raise Http404

    data = {'entity': product_list,
            'paginator': paginator
    }
    return render(request, 'index.html', data)


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user: login(request, user)
#             return HttpResponseRedirect(reverse("usuarios:index"))
#         else:
#             return render(request, "usuarios/login.html", { “msj": “Credenciales incorrectas" })
#     return render(request, "usuarios/login.html")
