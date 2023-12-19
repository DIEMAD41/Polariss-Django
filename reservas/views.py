import codecs
import json
import os

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from Polariss import settings
from reservas.models import ReservaVuelo
from .forms import ReservaVueloForm

#VISTAS BASADAS EN CLASES PARA RESERVACIONES DE VUELOS
class ReservacionVListView(ListView):
    #1.nombre del template que va a utilizar
    template_name = 'reservas/reservasV.html'
    #2. nombre del modelo
    model = ReservaVuelo
    #3. Nombre del contexto
    context_object_name = "reservas"
    #4. Paginacion
    paginate_by = 10

class ReservacionVAllListView(ListView):
    #1.nombre del template que va a utilizar
    template_name = 'reservas/reservasV_list.html'
    #2. nombre del modelo
    model = ReservaVuelo
    #3. Nombre del contexto
    context_object_name = "reservas"
    #4. Paginacion
    paginate_by = 10

class ReservacionVCreateView(CreateView):
    template_name = 'reservas/reservasV_new.html'
    form_class = ReservaVueloForm
    success_url = reverse_lazy('reservacionesV_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        json_path = os.path.join(settings.BASE_DIR, 'static/assets/js/cities.json')

        with codecs.open(json_path, 'r', encoding='utf-8-sig') as json_file:  # Usa 'utf-8-sig'
            data = json.load(json_file)

        context['cities_json'] = json.dumps(data)

        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Reserva creada exitosamente.')
        return response
