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
from .models import Especialidad, Plato, Pedido
from .carrito import Carrito

#from .apps import PlatoForm,PedidoForm
#from apps.Pedido.models import Plato,Pedido
#from apps.Pedido.carrito import Carrito
# Create your views here.


def promociones(request):
    lista_platos = Plato.objects.all()
    return render(request,'Pedido/promociones.html',{'platos': lista_platos})

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
    lista = carrito.lista()
    for id_plato in lista:
        print('LISTA DE PLATOS:',id_plato)
    
    id_user = request.POST['username']
    persona = Persona.objects.get(user_id=id_user)
    print('PERSONA:',persona.cuil)

    #class Pedido(models.Model):
    #cod_pedido = models.AutoField(primary_key=True)
    #fecha_pedido = models.DateTimeField(auto_now_add=True)
    #persona = models.ForeignKey(Persona,blank=False,null=False,on_delete=models.CASCADE)
    #hora_entrega_desde = models.TimeField(auto_noe)
    #hora_entrega_hasta = models.TimeField(blank= True)
    #estado_entrega = models.ForeignKey(EstadoEntrega, on_delete=models.CASCADE)
    #platos = models.ManyToManyField(Plato)
    #modo_entrega = models.ForeignKey(ModalidadEntrega,on_delete=models.CASCADE) 
    #cadete = models.ForeignKey(cadete,related_name='cadete',blank=True,null=True,on_delete=models.CASCADE)
    #curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)

    pedido = Pedido.objects.create()
    pedido.save(persona=persona,estado_entrega=1)


    carrito.limpiar()
    return redirect(to='Pedido:promociones')
    


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
            return redirect(reverse('Administrador'))
    else:
        pedido_form = PedidoForm(prefix='pedido')
    return render(request,'Pedido/RegistroDePedido.html',{'pedido_form': pedido_form})

def editar_plato(request, pk):
    plato = Plato.objects.get(codigo_plato=pk)
    return render(request,'Pedido/EditarPlato.html',{'plato':plato})

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

