from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from proveedores.forms import ProveedorForm
from proveedores.models import Proveedor
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .data import proveedores as mis_proveedores


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


#VISTAS BASADAS EN CLASES
class ProveedorListView(ListView):
    # Este fragmento de codigo es para llenar datos de data.py en nuestra BD
    
    #1.nombre del template que va a utilizar
    template_name = 'proveedores/proveedores_list.html'
    #2. nombre del modelo
    model = Proveedor
    #3. Nombre del contexto
    context_object_name = "proveedores"
    #4. Paginacion
    paginate_by = 10

#Recuerda editar el form para personalizar los campos que vas a manejar
class ProveedorCreateView(CreateView):
    #1. Especificar al template que responde a la vista
    template_name = 'proveedores/proveedores_new.html'
    #2. Especificar la forma
    form_class = ProveedorForm
    #3. Redireccionar
    success_url = reverse_lazy('proveedores:proveedor_list')

    #Sobreescribimos el metodo form_valid para mandar el mensaje de exito
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Proveedor creado exitosamente.')
        return response

    #Este metedo se ejecuta cuando el form es valido usalo solo si tienes un campo que se llena automaticamente
'''
    def form_valid(self, form):
        #Contenido del metodo
        return super(ProveedorCreateView, self).form_valid(form)
'''

class ProveedorUpdateView(UpdateView):
    template_name = 'proveedores/proveedores_update.html'
    # Si quieres editar todos los campos del form usa este codigo:
    form_class = ProveedorForm
    #Para editar solo campos especificos usa fields
    #fields = ['nombrec','telefenoc','usuarioc','passwordc','edadc','localidad']
    model = Proveedor
    success_url = reverse_lazy('proveedores:proveedor_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Proveedor modificado exitosamente.')
        return response

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedores/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedores:proveedor_list')
    context_object_name = 'proveedor'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Proveedor eliminado exitosamente.')
        return response