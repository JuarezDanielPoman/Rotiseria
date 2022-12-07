from urllib import request
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from apps.Pedido.models import Plato
from apps.Pedido.models import Pedido
from apps.Usuario.forms import *
from apps.Usuario.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import *
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):    
    return render(request, 'base/home.html')

#def administrador(request):
#    return render(request, 'base/baseAdministrador.html')


def registrarUsuario(request):
    
    domicilio_form = DomicilioForm(request.POST, prefix='domicilio')
    persona_form = PersonaForm(request.POST, prefix='persona')
    telefono_form = TelefonoForm(request.POST, prefix='telefono')
    formulario = CustomUserCreationForm(request.POST,prefix='formulario')
    if request.method == 'POST':
        if formulario.is_valid() and domicilio_form.is_valid() and persona_form.is_valid() and telefono_form.is_valid():
            p=persona_form.save(commit=False)
            f=formulario.save(commit=False)
            d=domicilio_form.save(commit=False)
            t=telefono_form.save(commit=False)
            
            p.user_username=f.username
            p.user_password=f.password
            f.first_name=p.nombre
            f.last_name=p.apellido
            f.email=p.email
            p.user_email=f.email

            t.save()
            d.save()
            
            p.domicilio_id=d.cod_domicilio
            p.telefono_id=t.id

            f.save()
            
            obtener_id_user = User.objects.get(id=f.id)
            p.user_id=obtener_id_user.pk
            p.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return render(request, 'base/home.html')
        else:
            domicilio_form = DomicilioForm(prefix='domicilio')
            persona_form = PersonaForm(prefix='persona')
            telefono_form = TelefonoForm(prefix='telefono')
            formulario = CustomUserCreationForm(prefix='formulario')
    return render(request,'Usuario/CrearUsuario.html',{'usuario':formulario,'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form})


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
            messages.success(request, 'Hola, ')
            return render(request, 'base/home.html')
            #return HttpResponseRedirect(reverse('baseCadete'))
        else:
            messages.error(request, 'Usuario y/o contraseña incorrecta')
            return render(request, 'base/home.html')
    return render(request, 'base/home.html')

@login_required(login_url='Usuario:login')
@permission_required('Persona.add_persona', raise_exception=True)
def creacion_cliente(request):
    if (request.method == 'POST'):
        domicilio_form = DomicilioForm(request.POST, prefix='domicilio')
        persona_form = PersonaForm(request.POST, prefix='persona')
        telefono_form = TelefonoForm(request.POST, prefix='telefono')
        if domicilio_form.is_valid() and persona_form.is_valid() and telefono_form.is_valid():
            p=persona_form.save(commit=False)
            d=domicilio_form.save(commit=False)
            t=telefono_form.save(commit=False)
            t.save()

            d.save()

            p.domicilio_id=d.cod_domicilio
            p.telefono_id=t.id
            p.save()

            messages.success(request,'¡PERSONA INGRESADA CORRECTAMENTE!')
            return redirect(reverse('Usuario:persona_detalle', args={p.id}))
    else:
        domicilio_form = DomicilioForm(prefix='domicilio')
        persona_form = PersonaForm(prefix='persona')
        telefono_form = TelefonoForm(prefix='telefono')
    return render(request,'Usuario/RegistroDeClientes.html',{'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form})

@login_required(login_url='Usuario:login')
@permission_required('Persona.add_cadete', raise_exception=True)
def creacion_cadete(request):
    if (request.method == 'POST'):
        usuario = CustomUserCreationForm(request.POST,prefix='formulario')
        domicilio_form = DomicilioForm(request.POST, prefix='domicilio')
        persona_form = CadeteForm(request.POST, prefix='persona')
        telefono_form = TelefonoForm(request.POST, prefix='telefono')
        if usuario.is_valid() and domicilio_form.is_valid() and persona_form.is_valid() and telefono_form.is_valid():
            f=usuario.save(commit=False)
            p=persona_form.save(commit=False)
            d=domicilio_form.save(commit=False)
            t=telefono_form.save(commit=False)

            p.user_username=f.username
            p.user_password=f.password
            f.first_name=p.nombre
            f.last_name=p.apellido
            f.email=p.email
            p.user_email=f.email
            p.user_is_staff=True

            t.save()
            d.save()
            
            p.domicilio_id=d.cod_domicilio
            p.telefono_id=t.id
            f.save()
            
            obtener_id_user = User.objects.get(id=f.id)
            p.user_id=obtener_id_user.pk
            p.save()
            #print(request.post['persona'])
            messages.success(request,'Se ha agregado correctamente la persona {}'.format(p,d,t))
            return redirect(reverse('Usuario:persona_detalle', args={p.id}))
    else:
        domicilio_form = DomicilioForm(prefix='domicilio')
        persona_form = CadeteForm(prefix='persona')
        telefono_form = TelefonoForm(prefix='telefono')
        usuario = CustomUserCreationForm(prefix='formulario')

    return render(request,'Usuario/RegistroDeCadetes.html',{'usuario': usuario,'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form})

@login_required(login_url='Usuario:login')
def editar_cadete(request,pk):

    cadete_editar = Cadete.objects.get(persona_ptr_id=pk)
    #id_user = User.objects.get(username=cadete_editar.user)
    id_user = cadete_editar.user.pk
    print("USUARIO CADETE: ", cadete_editar.user.pk)
    #print("CODIGO DE USUARIO CADETE: ", id_user.pk)
    
    if (request.method == 'POST'):
        print("ENTRA AL POST")
        cadete_form = CadeteForm(request.POST,prefix='persona', instance=cadete_editar)
        domicilio_cadete = DomicilioForm(request.POST,prefix='domicilio')
        telefono_cadete = TelefonoForm(request.POST,prefix='telefono')
        persona_form = PersonaForm(prefix='persona', instance=cadete_editar)

        if cadete_form.is_valid() and domicilio_cadete.is_valid() and telefono_cadete.is_valid():
            persona = persona_form.save(commit=False)
            domicilio = domicilio_cadete.save(commit=False)
            telefono = telefono_cadete.save(commit=False)
            cadet = cadete_form.save(commit=False)
            
            domicilio.save()
            telefono.save()

            persona.cuil = cadet.cuil
            persona.nombre = cadet.nombre
            persona.apellido = cadet.apellido
            persona.fecha_nacimiento = cadet.fecha_nacimiento
            persona.email = cadet.email
            persona.user_id = id_user
            persona.domicilio_id = domicilio.cod_domicilio
            persona.telefono_id = telefono.id
            
            persona.save()
            cadet.save()
            
            print("ANTES DEL RETUN POST")
            return redirect(to=('Usuario:lista_de_cadetes'))
        print("no entra al if")
    else:
        cadete_form = CadeteForm(prefix='persona', instance=cadete_editar)
        domicilio_cadete = DomicilioForm(prefix='domicilio', instance=cadete_editar.domicilio)
        telefono_cadete = TelefonoForm(prefix='telefono', instance=cadete_editar.telefono)
        return render(request,'Usuario/Cadete.html',{'cadete_form':cadete_form, 'domicilio_cadete':domicilio_cadete, 'telefono_cadete':telefono_cadete})


@login_required(login_url='Usuario:login')
@permission_required('Persona.view_persona', raise_exception=True)
def persona_detalle(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request,'Usuario/detalle.html',{'persona': persona})

@login_required(login_url='Usuario:login')
#@permission_required('Persona.delete_persona', raise_exception=True)
def persona_delete(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            persona = get_object_or_404(Persona, pk=request.POST['id'])
            persona.delete()
            messages.success(request,
            'Se ha eliminado la persona {}'.format(persona))
    return render(request,'Usuario/detalle.html')

@login_required(login_url='Usuario:login')
def persona_delete_lista(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            persona = get_object_or_404(Persona, pk=request.POST['id'])
            persona.delete()
            messages.success(request,
            'Se ha eliminado la persona {}'.format(persona))
    listaPersonas = Persona.objects.all()
    return render(request,'Usuario/ListaDePersonas.html',{'personas': listaPersonas})

@login_required(login_url='Usuario:login')
def cadete_delete(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            persona = get_object_or_404(Cadete, pk=request.POST['id'])
            persona.delete()
            messages.success(request,'Se ha eliminado la persona {}'.format(persona))
    #listaPersonas = cadete.objects.all()
    return redirect(to='Usuario:lista_de_cadetes')



@login_required(login_url='Usuario:login')
def persona_edit(request, pk):
    persona = get_object_or_404(Persona, pk=pk)

    if request.method == 'POST':
        domicilio_form = DomicilioForm(request.POST, prefix='domicilio')
        persona_form = PersonaForm(request.POST, prefix='persona',instance=persona)
        telefono_form = TelefonoForm(request.POST, prefix='telefono')
        
        if domicilio_form.is_valid() and persona_form.is_valid() and telefono_form.is_valid():
            p=persona_form.save(commit=False)
            d=domicilio_form.save(commit=False)
            t=telefono_form.save(commit=False)
            t.save()
            
            d.save()

            p.domicilio_id=d.cod_domicilio
            p.telefono_id=t.id
            p.save()
            messages.success(request,'¡DATOS MODIFICADOS CORRECTAMENTE!')
            return redirect(reverse('Usuario:persona_detalle', args={p.id}))
    else:
        persona_form = PersonaForm(prefix='persona', instance=persona)
        domicilio_form = DomicilioForm(prefix='domicilio', instance=persona.domicilio)
        telefono_form = TelefonoForm(prefix='telefono',instance=persona.telefono)
    return render(request,'Usuario/persona_edit.html',{'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form, 'persona':persona})

@login_required(login_url='Usuario:login')
@permission_required('Persona.view_cadete', raise_exception=True)
def lista_cadetes(request):
    listaCadetes = Cadete.objects.all()
    return render(request,'Usuario/ListaDeCadetes.html',{'cadetes': listaCadetes})

@login_required(login_url='Usuario:login')
@permission_required('Persona.view_persona', raise_exception=True)
def lista_personas(request):
    listaClientes = Persona.objects.all()
    return render(request,'Usuario/ListaDePersonas.html',{'personas': listaClientes})

@login_required(login_url='Usuario:login')
def buscar_personas(request):
    programas = Persona.objects.all()

    if 'buscar' in request.GET:
        buscar_persona = programas.filter(apellido__icontains=request.GET['buscar'])
    print(request.GET['buscar'])
    return render(request, 'Usuario/ListaDePersonas.html',
                  {'personas': buscar_persona})

@login_required(login_url='Usuario:login')
def buscar_cadetes(request):
    busqueda = request.POST.get("buscar")
    product_list = Cadete.objects.order_by('nombre')
    page = request.GET.get('page', 1)

    if busqueda:
        product_list = Cadete.objects.filter(
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


@login_required(login_url='Usuario:login')
@permission_required('Persona.view_persona', raise_exception=True)
def estadisticas(request):
            pedidos = Pedido.objects.all()
            platos = Plato.objects.all()
            cadetes = Cadete.objects.all()
            return render(request,'base/Estadistica.html',{'estadistica':pedidos,'platos':platos,'cadetes':cadetes})

