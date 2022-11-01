from tkinter import Menu
from xmlrpc.client import DateTime
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required
from apps.Pedido.forms import PlatoForm,PedidoForm
from apps.Pedido.models import Plato,Pedido

# Create your views here.

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

def RegistroPedidoCliente(request):
    #formulario
    lista_pedido = Plato.objects.all()
    return render(request,'Pedido/RegistroPedidoCliente.html',{'pedido': lista_pedido})


def menu_detalle(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    return render(request,'Pedido/detalle.html',{'plato': plato})

#@permission_required(Usuario.add_persona', raise_exception=True)
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


def lista_pedidos(request):
    listaPedidos = Pedido.objects.all()
    return render(request,'Pedido/ListaDepedidos.html',{'pedidos': listaPedidos})


def lista_pedidos_cadetes(request):
    listaPedidos = Pedido.objects.all()
    return render(request,'Pedido/listapedidoscadete.html',{'pedidos': listaPedidos})


#@permission_required(Usuario.add_persona', raise_exception=True)
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


def lista_pedidos(request):
    listaPedidos = Pedido.objects.all()
    return render(request,'Pedido/ListaDepedidos.html',{'pedidos': listaPedidos})


def lista_pedidos_cadetes(request):
    listaPedidos = Pedido.objects.all()
    return render(request,'Pedido/listapedidoscadete.html',{'pedidos': listaPedidos})


def lista_menus(request):
    listamenus = Plato.objects.all()
    return render(request,'Pedido/listademenus.html',{'menus': listamenus})

def menu_delete(request):
    if request.method == 'POST':
        if 'codigo_plato' in request.POST:
            menu = get_object_or_404(Plato, pk=request.POST['codigo_plato'])
            menu.delete()
            messages.success(request,
            'Se ha eliminado la persona {}'.format(menu))
    menus = Plato.objects.all()
    return render(request,
                  'Pedido/listademenus.html',{'menus': menus})

