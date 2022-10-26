from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from apps.Pedido.forms import PlatoForm
from apps.Pedido.models import Plato

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



def menu_detalle(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    return render(request,
                  'Pedido/detalle.html',
                  {'plato': plato})
