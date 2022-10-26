from audioop import reverse
from pyexpat.errors import messages
from django.shortcuts import redirect, render

from apps.Pedido.forms import PlatoForm
from apps.Pedido.models import Plato

# Create your views here.

def creacion_menu(request):
    if (request.method == 'POST'):
        plato_form = PlatoForm(request.POST, prefix='menu')
        if plato_form.is_valid():
            p=plato_form.save(commit=True)
            messages.success(request,
            'Se ha agregado correctamente la persona {}'.format(p))
            return redirect(reverse('Usuario:detalle', args={p.id}))
    else:
        plato_form = PlatoForm(prefix='menu')
    return render(request,'Pedido/RegistroDeMenu.html',{'plato_form': plato_form})

def promociones(request):
    lista_platos = Plato.objects.all()
    return render(request,'Pedido/promociones.html',{'platos': lista_platos})