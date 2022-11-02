from tkinter import Menu
from xmlrpc.client import DateTime
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from apps.Pedido.forms import PlatoForm,PedidoForm
from apps.Pedido.models import Plato,Pedido
from django.contrib.auth.decorators import login_required

from .forms import PlatoForm, PedidoForm
from .models import Plato, Pedido
from .carrito import Carrito

#from .apps import PlatoForm,PedidoForm
#from apps.Pedido.models import Plato,Pedido
#from apps.Pedido.carrito import Carrito
# Create your views here.
@login_required(login_url='Usuario:login')
def creacion_menu(request):
    if (request.method == 'POST'):
        plato_form = PlatoForm(request.POST, prefix='menu')
        if plato_form.is_valid():
            p=plato_form.save(commit=True)
            messages.success(request,
            'Se ha agregado correctamente el plato {}'.format(p))
            return redirect(reverse('Pedido:menu_detalle', args={p.codigo_plato}))
    else:
        plato_form = PlatoForm(prefix='menu')
    return render(request,'Pedido/RegistroDeMenu.html',{'plato_form': plato_form})

def promociones(request):
    lista_platos = Plato.objects.all()
    return render(request,'Pedido/promociones.html',{'platos': lista_platos})

#Vistas para el Carrito
@login_required(login_url='Usuario:login')
def CarritoPedidoCliente(request):
    return render(request,'Pedido/CarritoPedidoCliente.html',{'carrito': request.session['carrito']})

def agregar_plato_carrito(request, pk):
    print("Entra a agregar")
    carrito = Carrito(request)
    plato = Plato.objects.get(codigo_plato=pk)
    print("Plato: ", plato)
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

@login_required(login_url='Usuario:login')
def procesar_compra(request):
    carrito = Carrito(request)
    #lista_platos_carrito = request.session.carrito.items
    #print('LISTA DE PLATOS:',lista_platos_carrito)
    carrito.limpiar()
    return redirect(to='Pedido:promociones')

@login_required(login_url='Usuario:login')
def menu_detalle(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    return render(request,'Pedido/detalle.html',{'plato': plato})

#@permission_required(Usuario.add_persona', raise_exception=True)
@login_required(login_url='Usuario:login')
def creacion_pedido(request):
    if (request.method == 'POST'):
        pedido_form = PedidoForm(request.POST, prefix='pedido')
        if pedido_form.is_valid():
            p=pedido_form.save(commit=True)
            messages.success(request,
            'Se ha agregado correctamente el plato {}'.format(p))
            return redirect(reverse('Pedido:menu_detalle', args={p.cod_pedido}))
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


#@permission_required(Usuario.add_persona', raise_exception=True)
@login_required(login_url='Usuario:login')
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

@login_required(login_url='Usuario:login')
def lista_menus(request):
    listamenus = Plato.objects.all()
    return render(request,'Pedido/listademenus.html',{'menus': listamenus})

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

