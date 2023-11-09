from django.shortcuts import render, redirect
from clientes.models import Cliente
from django.contrib import messages

from .forms import ClienteForm
# Create your views here.
def clientes(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes': clientes
    }
    response = render(request, 'clientes/clientes.html', context=data)
    response['X-Frame-Options'] = 'ALLOW-FROM *'
    return response

def agregar_cliente(request):
    mensaje_error = None

    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            cliente = formulario.save()
            if cliente.idcliente:
                return redirect('clientes')
            else:
                mensaje_error = 'Error al guardar el cliente'
        else:
            mensaje_error = 'Formulario no válido'

    else:
        formulario = ClienteForm()

    return render(request, 'clientes', {'formulario': formulario, 'mensaje_error': mensaje_error})