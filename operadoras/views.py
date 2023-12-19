from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from operadoras.forms import OperadoraForm
from operadoras.models import Operadoras
from django.urls import reverse_lazy
from .data import operadoras as mis_operadoras

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


#VISTAS BASADAS EN CLASES
class OperadoraListView(ListView):

    #1.nombre del template que va a utilizar
    template_name = 'operadoras/operadoras_list.html'
    #2. nombre del modelo
    model = Operadoras
    #3. Nombre del contexto
    context_object_name = "operadoras"
    #4. Paginacion
    paginate_by = 10

#Recuerda editar el form para personalizar los campos que vas a manejar
class OperadoraCreateView(CreateView):
    #1. Especificar al template que responde a la vista
    template_name = 'operadoras/operadora_new.html'
    #2. Especificar la forma
    form_class = OperadoraForm
    #3. Redireccionar
    success_url = reverse_lazy('operadoras:operadoras_list')

    #Sobreescribimos el metodo form_valid para mandar el mensaje de exito
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Operadora creada exitosamente.')
        return response

    #Este metedo se ejecuta cuando el form es valido usalo solo si tienes un campo que se llena automaticamente
    def form_valid(self, form):
        #Contenido del metodo
        return super(OperadoraCreateView, self).form_valid(form)

class OperadoraUpdateView(UpdateView):
    template_name = 'operadoras/operadora_update.html'
    # Si quieres editar todos los campos del form usa este codigo:
    form_class = OperadoraForm
    #Para editar solo campos especificos usa fields
    #fields = ['nombrec','telefenoc','usuarioc','passwordc','edadc','localidad']
    model = Operadoras
    success_url = reverse_lazy('operadoras:operadoras_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Operadora modificada exitosamente.')
        return response

class OperadoraDeleteView(DeleteView):
    model = Operadoras
    template_name = 'operadoras/operadora_confirm_delete.html'
    success_url = reverse_lazy('operadoras:operadoras_list')
    context_object_name = 'operadora'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Operadora eliminada exitosamente.')
        return response
