from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from paquetes.models import Paquetes
from django.contrib import messages
import json
from .forms import PaqueteForm

# Create your views here.
def paquetes(request):
    paquetes = Paquetes.objects.all()
    data = {
        'paquetes': paquetes
    }
    response = render(request, 'paquetes/paquetes.html', context=data)
    response['X-Frame-Options'] = 'ALLOW-FROM *'
    return response

#VISTAS BASADAS EN CLASES
class PaqueteListView(ListView):
    # Este fragmento de codigo es para llenar datos de data.py en nuestra BD


     # Cargar los agentes
    '''
    print("Iniciar la carga de agentes")
    for agente in mis_agentes:
        print("Grabando . . . ", agente)
        Agentes.objects.create(
            nombreg=agente[1],
            telefenog=agente[2],
            usuariog=agente[3],
            passwordg=agente[4],
            saldo=agente[5],
            edadg=agente[6],
            localidadg = agente[7]
        )
    '''

    #1.nombre del template que va a utilizar
    template_name = 'paquetes/paquetes_list.html'
    #2. nombre del modelo
    model = Paquetes
    #3. Nombre del contexto
    context_object_name = "paquetes"
    #4. Paginacion
    paginate_by = 10

#Recuerda editar el form para personalizar los campos que vas a manejar
class PaqueteCreateView(CreateView):
    #1. Especificar al template que responde a la vista
    template_name = 'paquetes/paquetes_new.html'
    #2. Especificar la forma
    form_class = PaqueteForm
    #3. Redireccionar
    success_url = reverse_lazy('paquetes:paquetes_list')



    #Sobreescribimos el metodo form_valid para mandar el mensaje de exito
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Paquete creado exitosamente.')
        return response

    #Este metedo se ejecuta cuando el form es valido usalo solo si tienes un campo que se llena automaticamente
    def form_valid(self, form):
        #Contenido del metodo
        return super(PaqueteCreateView, self).form_valid(form)

class PaqueteUpdateView(UpdateView):
    template_name = 'paquetes/paquetes_update.html'
    # Si quieres editar todos los campos del form usa este codigo:
    form_class = PaqueteForm
    #Para editar solo campos especificos usa fields
    #fields = ['nombrec','telefenoc','usuarioc','passwordc','saldo','edadc','localidad']
    model = Paquetes
    success_url = reverse_lazy('paquetes:paquetes_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Paquete modificado exitosamente.')
        return response

class PaqueteDeleteView(DeleteView):
    model = Paquetes
    template_name = 'paquetes/paquetes_confirm_delete.html'
    success_url = reverse_lazy('paquetes:paquetes_list')
    context_object_name = 'paquetes'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Paquete eliminado exitosamente.')
        return response