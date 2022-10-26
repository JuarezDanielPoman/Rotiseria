from audioop import reverse
from pyexpat.errors import messages
from django.shortcuts import redirect, render

from apps.Pedido.forms import PlatoForm

# Create your views here.

def creacion_menu(request):
    if (request.method == 'POST'):
        plato_form = PlatoForm(request.POST, prefix='menu')
        if PlatoForm.is_valid():
            p=plato_form.save(commit=True)
            messages.success(request,
            'Se ha agregado correctamente la persona {}'.format(p))
            return redirect(reverse('Usuario:detalle', args={p.id}))
    else:
        plato_form = PlatoForm(prefix='menu')
    return render(request,'Pedido/RegistroDeMenu.html',{'plato_form': plato_form})
 