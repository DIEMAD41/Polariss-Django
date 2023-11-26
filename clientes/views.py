from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from clientes.models import Cliente
from django.contrib import messages
import json
from .forms import ClienteForm
from .data import clientes as mis_clientes

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


#VISTAS BASADAS EN CLASES
class ClienteListView(ListView):
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
    template_name = 'clientes/clientes_list.html'
    #2. nombre del modelo
    model = Cliente
    #3. Nombre del contexto
    context_object_name = "clientes"
    #4. Paginacion
    paginate_by = 10

#Recuerda editar el form para personalizar los campos que vas a manejar
class ClienteCreateView(CreateView):
    #1. Especificar al template que responde a la vista
    template_name = 'clientes/clientes_new.html'
    #2. Especificar la forma
    form_class = ClienteForm
    #3. Redireccionar
    success_url = reverse_lazy('clientes:cliente_list')

    #Sobreescribimos el metodo form_valid para mandar el mensaje de exito
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente creado exitosamente.')
        return response

    #Este metedo se ejecuta cuando el form es valido usalo solo si tienes un campo que se llena automaticamente
'''
    def form_valid(self, form):
        #Contenido del metodo
        return super(ClienteCreateView, self).form_valid(form)
'''

class ClienteUpdateView(UpdateView):
    template_name = 'clientes/clientes_update.html'
    # Si quieres editar todos los campos del form usa este codigo:
    form_class = ClienteForm
    #Para editar solo campos especificos usa fields
    #fields = ['nombrec','telefenoc','usuarioc','passwordc','edadc','localidad']
    model = Cliente
    success_url = reverse_lazy('clientes:cliente_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente modificado exitosamente.')
        return response

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('clientes:cliente_list')
    context_object_name = 'cliente'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente eliminado exitosamente.')
        return response
