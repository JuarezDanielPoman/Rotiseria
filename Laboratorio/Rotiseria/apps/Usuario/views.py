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
    zona_form = ZonaDomicilioForm(request.POST, prefix='zona')
    formulario = CustomUserCreationForm(request.POST,prefix='formulario')
    if request.method == 'POST':
        if formulario.is_valid() and domicilio_form.is_valid() and persona_form.is_valid() and telefono_form.is_valid() and zona_form.is_valid():
            p=persona_form.save(commit=False)
            f=formulario.save(commit=False)
            d=domicilio_form.save(commit=False)
            t=telefono_form.save(commit=False)
            z=zona_form.save(commit=False)
            
            p.user_username=f.username
            p.user_password=f.password
            f.first_name=p.nombre
            f.last_name=p.apellido
            f.email=p.email
            p.user_email=f.email

            t.save()
            z.save()
            
            d.zona_id=z.cod_zona
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
            zona_form = ZonaDomicilioForm(prefix='zona')
            formulario = CustomUserCreationForm(prefix='formulario')
    return render(request,'Usuario/CrearUsuario.html',{'usuario':formulario,'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form,'zona_form': zona_form})


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

@login_required(login_url='Usuario:login')
@permission_required('Persona.add_cadete', raise_exception=True)
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

            #print(request.post['persona'])
            messages.success(request,'Se ha agregado correctamente la persona {}'.format(p,d,t,z))
            return redirect(reverse('Usuario:persona_detalle', args={p.id}))
    else:
        domicilio_form = DomicilioForm(prefix='domicilio')
        persona_form = CadeteForm(prefix='persona')
        telefono_form = TelefonoForm(prefix='telefono')
        zona_form = ZonaDomicilioForm(prefix='zona')
    return render(request,'Usuario/RegistroDeCadetes.html',{'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form,'zona_form': zona_form})

@login_required(login_url='Usuario:login')
def persona_detalle(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request,'Usuario/detalle.html',{'persona': persona})

@login_required(login_url='Usuario:login')
def persona_delete(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            persona = get_object_or_404(Persona, pk=request.POST['id'])
            persona.delete()
            messages.success(request,
            'Se ha eliminado la persona {}'.format(persona))
    return render(request,
                  'Usuario/detalle.html')

@login_required(login_url='Usuario:login')
def persona_delete_lista(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            persona = get_object_or_404(Persona, pk=request.POST['id'])
            persona.delete()
            messages.success(request,
            'Se ha eliminado la persona {}'.format(persona))
    listaPersonas = Persona.objects.all()
    return render(request,
                  'Usuario/ListaDePersonas.html',{'personas': listaPersonas})

@login_required(login_url='Usuario:login')
def cadete_delete(request):
    if request.method == 'POST':
        if 'id' in request.POST:
            persona = get_object_or_404(cadete, pk=request.POST['id'])
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
    return render(request,'Usuario/persona_edit.html',{'persona_form': persona_form,'domicilio_form': domicilio_form,'telefono_form': telefono_form,'zona_form': zona_form, 'persona':persona})

@login_required(login_url='Usuario:login')
@permission_required('Persona.view_cadete', raise_exception=True)
def lista_cadetes(request):
    listaCadetes = cadete.objects.all()
    return render(request,'Usuario/ListaDeCadetes.html',{'cadetes': listaCadetes})

@login_required(login_url='Usuario:login')
@permission_required('Persona.view_persona', raise_exception=True)
def lista_personas(request):
    listaPersonas = Persona.objects.all()
    return render(request,'Usuario/ListaDePersonas.html',{'personas': listaPersonas})

@login_required(login_url='Usuario:login')
def buscar_personas(request):
    programas = Persona.objects.all()

    if 'buscar' in request.GET:
        buscar_persona = programas.filter(nombre__icontains=request.GET['buscar'])
    print(request.GET['buscar'])
    return render(request, 'Usuario/ListaDePersonas.html',
                  {'personas': buscar_persona})

@login_required(login_url='Usuario:login')
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


    
@login_required
def estadisticas(request):
            pedidos = Pedido.objects.all()
            platos = Plato.objects.all()
            cadetes = cadete.objects.all()
            return render(request,'base/Estadistica.html',{'estadistica':pedidos,'platos':platos,'cadetes':cadetes})
         
# @login_required
# def estadisticas(request):
#     return render(request, 'cursos/estadisticas.html', {'cursos':curso.objects.all()})
    
# @login_required
# def estadisticas_1(request):
#     #if request.method == 'POST':
#             Cursos = curso.objects.all()
#             #Curso = get_object_or_404(curso,pk=request.POST['id_curso'])
            
#             #cantinscriptos = []
#             for data in Cursos:
#                 #cantinscriptos.append(len(Inscriptos.objects.filter(curso = data.id)))
#                 data.cant = len(Inscriptos.objects.filter(curso = data.id))
                 
#             #print(cantinscriptos)
#             return render(request,'cursos/estadisticascantinscriptos.html',{'cursos':Cursos})
#             # nombre_curso = Curso.nombrecurso
#             # Curso.delete()
#             # messages.success(request, 'Se ha eliminado exitosamente el curso {}'.format(nombre_curso))
#         # else:
#             # messages.error(request, 'Debe indicar qué Programa se desea eliminar')

# @login_required
# def estadisticas_2(request):
#     Cursos = curso.objects.all()
    
#     for data in Cursos:
#         data.cant = len(Inscriptos.objects.filter(curso = data.id))
#         data.cantP= len(PagoEfectivo.objects.filter(curso = data.id)) + len(PagoTarjeta.objects.filter(curso = data.id)) + len(PagoTransferencia.objects.filter(curso = data.id)) 
#         data.cantD= data.cant - data.cantP
    
#     return render(request,'cursos/estadisticascantpago.html',{'cursos':Cursos})    


# @login_required
# def estadisticas_3(request):
#     if request.method == 'POST':
#         fechaini = request.POST.get('id_anioinicio',None)
#         fechafin = request.POST.get('id_aniofin',None)
#         intervalo= curso.objects.filter(fechaini__range=(fechaini, fechafin))
#     return render (request,'cursos/listaCursosAnio.html',{'intervalo':intervalo,'fechaini':fechaini,'fechafin':fechafin})

  