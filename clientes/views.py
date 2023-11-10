from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from clientes.models import Cliente
from django.contrib import messages
import json
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
            messages.success(request, "Cliente Agregado")
            if cliente.idcliente:
                return redirect('clientes')
            else:
                mensaje_error = 'Error al guardar el cliente'
        else:
            mensaje_error = 'Formulario no válido'

    else:
        formulario = ClienteForm()

    return render(request, 'clientes.html', {'formulario': formulario, 'mensaje_error': mensaje_error})

def obtener_datos_cliente(request, cliente_id):
    try:
        cliente = Cliente.objects.get(idcliente=cliente_id)
        data = {
            'idcliente': cliente.idcliente,
            'nombrec': cliente.nombrec,
            'telefenoc': cliente.telefenoc,
            'usuarioc': cliente.usuarioc,
            'passwordc': cliente.passwordc,
            'edadc': cliente.edadc,
            'localidad': cliente.localidad
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

@csrf_exempt  # Desactivar CSRF para simplificar el ejemplo
def modificar_cliente(request, cliente_id):
    if request.method == 'POST':
        try:
            cliente = Cliente.objects.get(idcliente=cliente_id)
            data = json.loads(request.body)
            cliente.nombrec = data.get('nombrec', cliente.nombrec)
            cliente.telefenoc = data.get('telefenoc', cliente.telefenoc)
            cliente.usuarioc = data.get('usuarioc', cliente.usuarioc)
            cliente.passwordc = data.get('passwordc', cliente.passwordc)
            cliente.edadc = data.get('edadc', cliente.edadc)
            cliente.localidad = data.get('localidad', cliente.localidad)
            cliente.save()
            messages.success(request, "Cliente Modificado")
            return JsonResponse({'success': True})
        except Cliente.DoesNotExist:
            return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def eliminar_cliente(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        cliente = get_object_or_404(Cliente, idcliente=cliente_id)
        cliente.delete()
        messages.success(request, "Cliente Eliminado")
        return redirect('clientes')