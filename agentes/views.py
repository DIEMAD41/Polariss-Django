from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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



#VISTAS BASADAS EN CLASES
class AgenteListView(ListView):
    # Este fragmento de codigo es para llenar datos de data.py en nuestra BD
    '''
       # Cargar los clientes
        print("Iniciar la carga de clientes")
        for cliente in mis_clientes:
            print("Grabando . . . ", cliente)
            Cliente.objects.create(
                nombrec=cliente[0],
                telefenoc=cliente[1],
                usuarioc=cliente[2],
                passwordc=cliente[3],
                edadc=cliente[4],
                localidad=cliente[5]
            )
    '''
    #1.nombre del template que va a utilizar
    template_name = 'agentes/agentes_list.html'
    #2. nombre del modelo
    model = Agentes
    #3. Nombre del contexto
    context_object_name = "agentes"
    #4. Paginacion
    paginate_by = 10

#Recuerda editar el form para personalizar los campos que vas a manejar
class AgenteCreateView(CreateView):
    #1. Especificar al template que responde a la vista
    template_name = 'agentes/agentes_new.html'
    #2. Especificar la forma
    form_class = AgenteForm
    #3. Redireccionar
    success_url = reverse_lazy('agentes:agentes_list')

    #Sobreescribimos el metodo form_valid para mandar el mensaje de exito
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Agente creado exitosamente.')
        return response

    #Este metedo se ejecuta cuando el form es valido usalo solo si tienes un campo que se llena automaticamente
'''
    def form_valid(self, form):
        #Contenido del metodo
        return super(ClienteCreateView, self).form_valid(form)
'''

class AgenteUpdateView(UpdateView):
    template_name = 'agentes/agentes_update.html'
    # Si quieres editar todos los campos del form usa este codigo:
    form_class = AgenteForm
    #Para editar solo campos especificos usa fields
    #fields = ['nombrec','telefenoc','usuarioc','passwordc','saldo','edadc','localidad']
    model = Agentes
    success_url = reverse_lazy('agentes:agentes_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Agente modificado exitosamente.')
        return response

class AgenteDeleteView(DeleteView):
    model = Agentes
    template_name = 'agentes/agente_confirm_delete.html'
    success_url = reverse_lazy('agentes:agentes_list')
    context_object_name = 'agente'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Agente eliminado exitosamente.')
        return response
