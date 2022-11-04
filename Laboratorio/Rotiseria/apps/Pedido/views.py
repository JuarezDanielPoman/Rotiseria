from tkinter import Menu
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from apps.Pedido.forms import PlatoForm,PedidoForm
from apps.Pedido.models import Plato,Pedido
from django.contrib.auth.decorators import login_required

from apps.Usuario.models import Persona

from .forms import PlatoForm, PedidoForm
from .models import Especialidad, EstadoEntrega, ModalidadEntrega, Plato, Pedido, TipoPlato
from .carrito import Carrito
from django.utils.datastructures import MultiValueDictKeyError
#from .apps import PlatoForm,PedidoForm
#from apps.Pedido.models import Plato,Pedido
#from apps.Pedido.carrito import Carrito
# Create your views here.


def promociones(request):
    lista_platos_activos = Plato.objects.filter(vigencia_plato=True)
    #lista_platos = Plato.objects.filter(estado_promocion=True)
    lista_platos_promocion = lista_platos_activos.filter(estado_promocion=True)
    return render(request,'Pedido/promociones.html',{'platos': lista_platos_promocion})

def listarCategoriaPlato(request):
    lista_categoria = Especialidad.objects.all()
    print(lista_categoria)
    return render(request,'base/home.html',{'categorias': lista_categoria})

#Vistas para el Carrito
@login_required(login_url='Usuario:login')
def CarritoPedidoCliente(request):
    return render(request,'Pedido/CarritoPedidoCliente.html',{'carrito': request.session['carrito']})

def agregar_plato_carrito(request, pk):
    carrito = Carrito(request)
    plato = Plato.objects.get(codigo_plato=pk)
    carrito.agregar(plato)
    return redirect(to='Pedido:CarritoPedidoCliente')

def eliminar_plato_carrito(request, pk):
    carrito = Carrito(request)
    plato = Plato.objects.get(codigo_plato=pk)
    carrito.eliminar(plato)
    return redirect(to='Pedido:CarritoPedidoCliente')

def restar_plato_carrito(request, pk):
    carrito = Carrito(request)
    plato = Plato.objects.get(codigo_plato=pk)
    carrito.restar(plato)
    return redirect(to='Pedido:CarritoPedidoCliente')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(to='Pedido:CarritoPedidoCliente')

def procesar_compra(request):
    carrito = Carrito(request)
    id_user = request.POST['username']
    persona = Persona.objects.get(user_id=id_user)
    estadoentrega = EstadoEntrega.objects.get(estado_entrega=2)
    modoentrega = ModalidadEntrega.objects.get(modoentrega=1)
    print('PERSONA:',persona.cuil)

    entrega = EstadoEntrega.objects.get(estado_entrega=1)
    modalidad = ModalidadEntrega.objects.get(modoentrega=1)

    pedido = Pedido.objects.create()
    pedido.save(persona=persona,estado_entrega=1)

    lista = carrito.lista()
    for id_plato in lista:
        print('LISTA DE PLATOS:',id_plato)
        pedido.platos.add(id_plato)

    pedido.save()
    carrito.limpiar()
    return redirect(to='Pedido:promociones')

#VISTAS DE MUNÚS (PLATOS)
@login_required(login_url='Usuario:login')
@permission_required('Plato.add_plato', raise_exception=True)
def creacion_menu(request):
    if (request.method == 'POST'):
        plato_form = PlatoForm(request.POST, prefix='menu')
        if plato_form.is_valid():
            p=plato_form.save(commit=True)
            return redirect(reverse('Pedido:menu_detalle', args={p.codigo_plato}))
    else:
        plato_form = PlatoForm(prefix='menu')
    return render(request,'Pedido/RegistroDeMenu.html',{'plato_form': plato_form})

@login_required(login_url='Usuario:login')
def menu_detalle(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    return render(request,'Pedido/detalle.html',{'plato': plato})

@login_required(login_url='Usuario:login')
def menu_delete(request):
    if request.method == 'POST':
        if 'codigo_plato' in request.POST:
            menu = get_object_or_404(Plato, pk=request.POST['codigo_plato'])
            menu.delete()
            messages.success(request,
            'Se ha eliminado la persona {}'.format(menu))
    menus = Plato.objects.all()
    return render(request,'Pedido/listademenus.html',{'menus': menus})

@login_required(login_url='Usuario:login')
def menu_edit(request, pk):
    #MUESTRA EL TEMPLATE EDITAR 
    plato = Plato.objects.get(codigo_plato=pk)
    plato_form = PlatoForm(prefix='menu')
    return render(request,'Pedido/EditarPlato.html',{'plato_form': plato_form,'plato':plato})

@login_required(login_url='Usuario:login')
def menu_editado(request):
    #AQUÍ REALIZA LA MODIFICACION DEL PLATO
    id = request.POST['codigo_plato']
    plato = Plato.objects.get(codigo_plato=id)

    try:
        vigencia = request.POST['menu-vigencia_plato']
    except MultiValueDictKeyError:
            vigencia = 'Error'
    try:
        estado = request.POST['menu-estado_promocion']
    except MultiValueDictKeyError:
            estado = 'Error'
    nombre = request.POST['nombre_plato']
    precio = request.POST['precio_plato']
    tipo = request.POST['menu-tipo_plato']
    tipo_plato = TipoPlato.objects.get(tipo_plato=tipo)
    especialidad = request.POST['menu-especialidad']
    tipo_especialidad = Especialidad.objects.get(especialidad=especialidad)

    print('VERDADADERO:',vigencia)
    print('FALSO:',estado)

    if(vigencia == 'on'):
        plato.vigencia_plato = True
    else:
        plato.vigencia_plato = False

    if(estado =='on'):
        plato.estado_promocion = True
    else:
        plato.estado_promocion = False
    
    plato.nombre_plato = nombre
    plato.precio_plato= precio
    plato.tipo_plato = tipo_plato
    plato.especialidad = tipo_especialidad

    plato.save()
    return redirect(to='Administrador')



@login_required(login_url='Usuario:login')
@permission_required('Pedido.view_menus', raise_exception=True)
def lista_menus(request):
    listamenus = Plato.objects.all()
    return render(request,'Pedido/listademenus.html',{'menus': listamenus})




#VISTAS DE PEDIDO - ADMIN
#@permission_required(Usuario.add_persona', raise_exception=True)
@login_required(login_url='Usuario:login')
@permission_required('Pedido.add_pedido', raise_exception=True)
def creacion_pedido(request):
    if (request.method == 'POST'):
        pedido_form = PedidoForm(request.POST, prefix='pedido')
        if pedido_form.is_valid():
            p=pedido_form.save(commit=True)
            messages.success(request,
            'Se ha agregado correctamente el plato {}'.format(p))
            return redirect(reverse('Pedido:menu_detalle', args={p.codigo_pedido}))
    else:
        pedido_form = PedidoForm(prefix='pedido')
    return render(request,'Pedido/RegistroDePedido.html',{'pedido_form': pedido_form})

@login_required(login_url='Usuario:login')
def lista_pedidos(request):
    listaPedidos = Pedido.objects.all()
    return render(request,'Pedido/ListaDepedidos.html',{'pedidos': listaPedidos})

@login_required(login_url='Usuario:login')
def lista_pedidos_cadetes(request):
    listaPedidos = Pedido.objects.all()
    return render(request,'Pedido/listapedidoscadete.html',{'pedidos': listaPedidos})






# @login_required(login_url='Usuario:login')
# def pedido_edit(request, pk):
#     pedido = get_object_or_404(Pedido, pk=pk)
#     if request.method == 'POST' :
#         pedido_form = PedidoForm(request.POST,prefix='pedido')
#         if pedido_form.is_valid():
#             pedido=pedido_form.save(commit=True)
#         return redirect(reverse('Usuario:listaDepedidos', args={pedido.id}))
#     else:   
#         pedido_form = PedidoForm(prefix='pedido')
#         return render(request,'Pedido/listaDepedidos.html',args={pedido.id})
