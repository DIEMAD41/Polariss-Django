from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from proveedores.forms import ProveedorForm
from proveedores.models import Proveedor
# Create your views here.
def proveedores(request):
    proveedores = Proveedor.objects.all()
    data = {
        'proveedores': proveedores
    }
    return render(request, 'proveedores/proveedores.html', context=data)

def agregar_proveedor(request):
    mensaje_error = None
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            proveedor = formulario.save()
            messages.success(request, "Proveedor Agregado")
            if proveedor.idprov:
                return redirect('proveedores')
            else:
                mensaje_error = 'Error al guardar el proveedor'
        else:
            mensaje_error = 'Formulario no válido'

    else:
        formulario = ProveedorForm()

    return render(request, 'proveedores/proveedores.html', {'formulario': formulario, 'mensaje_error': mensaje_error})

def obtener_datos_proveedor(request, prov_id):
    try:
        proveedor = Proveedor.objects.get(idprov=prov_id)
        data = {
            'idprov': proveedor.idprov,
            'nombreprov': proveedor.nombreprov,
            'telefenoprov': proveedor.telefenoprov,
            'correoprov': proveedor.correoprov,
            'nombreop': proveedor.nombreop,
        }
        return JsonResponse(data)
    except Proveedor.DoesNotExist:
        return JsonResponse({'error': 'Proveedor no encontrado'}, status=404)

@csrf_exempt
def modificar_proveedor(request, prov_id):
    if request.method == 'POST':
        try:
            proveedor = Proveedor.objects.get(idprov=prov_id)
            data = json.loads(request.body)
            proveedor.nombreprov = data.get('nombreprov', proveedor.nombreprov)
            proveedor.telefenoprov = data.get('telefenoprov', proveedor.telefenoprov)
            proveedor.correoprov = data.get('correoprov', proveedor.correoprov)
            proveedor.nombreop = data.get('nombreop', proveedor.nombreop)
            proveedor.save()
            messages.success(request, "Proveedor Modificado")
            return JsonResponse({'success': True})
        except Proveedor.DoesNotExist:
            return JsonResponse({'error': 'Proveedor no encontrado'}, status=404)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_proveedor(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor_id')
        proveedor = get_object_or_404(Proveedor, idprov=proveedor_id)
        proveedor.delete()
        messages.success(request, "Proveedor Eliminado")
        return redirect('proveedores')