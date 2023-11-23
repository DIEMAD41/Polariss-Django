from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json

from operadoras.forms import OperadoraForm
from operadoras.models import Operadoras


# Create your views here.
def operadoras(request):
    operadoras = Operadoras.objects.all()
    data = {
        'operadoras': operadoras
    }
    response = render(request, 'operadoras/operadoras.html', context=data)
    response['X-Frame-Options'] = 'ALLOW-FROM *'
    return response

def agregar_operadora(request):
    mensaje_error = None

    if request.method == 'POST':
        formulario = OperadoraForm(request.POST)
        if formulario.is_valid():
            operadora = formulario.save()
            messages.success(request, "Operadora Agregada")
            if operadora.clave:
                return redirect('operadoras')
            else:
                mensaje_error = 'Error al guardar la operadora'
        else:
            mensaje_error = 'Formulario no válido'
        print("HOLA",formulario.errors,mensaje_error)
    else:
        formulario = OperadoraForm()
        print("HOLA2",formulario.errors)

    return render(request, 'operadoras/operadoras.html', {'formulario': formulario, 'mensaje_error': mensaje_error})


def obtener_datos_operadora(request, clave):
    try:
        operadora = Operadoras.objects.get(clave=clave)
        data = {
            'clave': operadora.clave,
            'nombre': operadora.nombre,
            'email': operadora.email,

        }
        return JsonResponse(data)
    except Operadoras.DoesNotExist:
        return JsonResponse({'error': 'Operadora no encontrad'}, status=404)


@csrf_exempt
def modificar_operadora(request, clave):
    if request.method == 'POST':
        try:
            operadora = Operadoras.objects.get(clave=clave)
            data = json.loads(request.body)
            operadora.nombre = data.get('nombre', operadora.nombre)
            operadora.email = data.get('email', operadora.email)
            operadora.save()
            messages.success(request, "Operadora Modificada")
            return JsonResponse({'success': True})
        except Operadoras.DoesNotExist:
            return JsonResponse({'error': 'Operadora no encontrada'}, status=404)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def eliminar_operadora(request):
    if request.method == 'POST':
        clave = request.POST.get('clave')
        print("Clave recibida:", clave)
        clave = get_object_or_404(Operadoras, clave=clave)
        clave.delete()
        messages.success(request, "Operadora Eliminada")
        return redirect('operadoras')