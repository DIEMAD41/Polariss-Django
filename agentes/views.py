from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from agentes.models import Agentes
from django.contrib import messages
import json

from .forms import AgenteForm
# Create your views here.
def agentes(request):
    agentes = Agentes.objects.all()
    data = {
        'agentes': agentes
    }
    response = render(request, 'agentes/agentes.html', context=data)
    response['X-Frame-Options'] = 'ALLOW-FROM *'
    return response

def agregar_agente(request):
    mensaje_error = None

    if request.method == 'POST':
        formulario = AgenteForm(request.POST)
        if formulario.is_valid():
            agente = formulario.save()
            messages.success(request, "Agente Agregado")
            if agente.idagente:
                return redirect('agentes')
            else:
                mensaje_error = 'Error al guardar el agente'
        else:
            mensaje_error = 'Formulario no válido'

    else:
        formulario = AgenteForm()

    return render(request, 'agentes/agentes.html', {'formulario': formulario, 'mensaje_error': mensaje_error})

def obtener_datos_agente(request, agente_id):
    try:
        agente = Agentes.objects.get(idagente=agente_id)
        data = {
            'idagente': agente.idagente,
            'nombreg': agente.nombreg,
            'telefenog': agente.telefenog,
            'usuariog': agente.usuariog,
            'passwordg': agente.passwordg,
            'edadg': agente.edadg,
            'saldo': agente.saldo,
            'localidadg': agente.localidadg
        }
        return JsonResponse(data)
    except Agentes.DoesNotExist:
        return JsonResponse({'error': 'Agente no encontrado'}, status=404)

@csrf_exempt  # Desactivar CSRF para simplificar el ejemplo (Considera la seguridad en un entorno de producción)
def modificar_agente(request, agente_id):
    if request.method == 'POST':
        try:
            agente = Agentes.objects.get(idagente=agente_id)
            data = json.loads(request.body)
            agente.nombreg = data.get('nombreg', agente.nombreg)
            agente.telefenog = data.get('telefenog', agente.telefenog)
            agente.usuariog = data.get('usuariog', agente.usuariog)
            agente.passwordg = data.get('passwordg', agente.passwordg)
            agente.edadg = data.get('edadg', agente.edadg)
            agente.saldo = data.get('saldo', agente.saldo)
            agente.localidadg = data.get('localidadg', agente.localidadg)
            agente.save()
            messages.success(request, "Agente Modificado")
            return JsonResponse({'success': True})
        except Agentes.DoesNotExist:
            return JsonResponse({'error': 'Agente no encontrado'}, status=404)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def eliminar_agente(request):
    if request.method == 'POST':
        agente_id = request.POST.get('agente_id')
        agente = get_object_or_404(Agentes, idagente=agente_id)
        agente.delete()
        messages.success(request, "Agente Eliminado")
        return redirect('agentes')