import codecs
import json
import os

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Polariss import settings
from reservas.models import ReservaVuelo, Venta, Pago
from .forms import ReservaVueloForm, VentaForm, PagoForm


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


class ReservacionUpdateView(UpdateView):
    template_name = 'reservas/reservasV_update.html'
    # Si quieres editar todos los campos del form usa este codigo:
    form_class = ReservaVueloForm
    #Para editar solo campos especificos usa fields
    #fields = ['nombrec','telefenoc','usuarioc','passwordc','edadc','localidad']
    model = ReservaVuelo
    success_url = reverse_lazy('reservacionesV_update')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Reserva modificado exitosamente.')
        return response

class ReservacionDeleteView(DeleteView):
    model = ReservaVuelo
    template_name = 'reservas/reservaV_confirm_delete.html'
    success_url = reverse_lazy('reservacionesV_delete')
    context_object_name = 'reserva'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Reserva eliminada exitosamente.')
        return response

#VENTAS
class VentasVAllListView(ListView):
    #1.nombre del template que va a utilizar
    template_name = 'reservas/venta_list.html'
    #2. nombre del modelo
    model = Venta
    #3. Nombre del contexto
    context_object_name = "ventas"
    #4. Paginacion
    paginate_by = 10

class VentasCreateView(CreateView):
    #1. Especificar al template que responde a la vista
    template_name = 'reservas/ventas_new.html'
    #2. Especificar la forma
    form_class = VentaForm
    #3. Redireccionar
    success_url = reverse_lazy('ventas')

    #Sobreescribimos el metodo form_valid para mandar el mensaje de exito
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente creado exitosamente.')
        return response


class VentasUpdateView(UpdateView):
    template_name = 'reservas/ventas_update.html'
    # Si quieres editar todos los campos del form usa este codigo:
    form_class = VentaForm
    #Para editar solo campos especificos usa fields
    #fields = ['nombrec','telefenoc','usuarioc','passwordc','edadc','localidad']
    model = Venta
    success_url = reverse_lazy('ventas')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cliente modificado exitosamente.')
        return response

class VentasDeleteView(DeleteView):
    model = Venta
    template_name = 'reservas/venta_confirm_delete.html'
    success_url = reverse_lazy('ventas')
    context_object_name = 'ventas'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Venta eliminada exitosamente.')
        return response



#VIEWS DE PAGO
class PagosListView(ListView):
    # Este fragmento de codigo es para llenar datos de data.py en nuestra BD
    #1.nombre del template que va a utilizar
    template_name = 'reservas/pago_list.html'
    #2. nombre del modelo
    model = Pago
    #3. Nombre del contexto
    context_object_name = "pagos"
    #4. Paginacion
    paginate_by = 10

class PagosCreateView(CreateView):
    template_name = 'reservas/pago_new.html'
    form_class = PagoForm
    success_url = reverse_lazy('pagos')

    def form_valid(self, form):
        # Llamada al form_valid de la clase base
        response = super().form_valid(form)

        # Obtener el objeto de venta asociado al pago
        venta = form.instance.venta
        print("Saldo:",venta.saldo)
        print("Monto:", form.instance.monto)
        # Restar el monto del pago al saldo de la venta
        venta.saldo -= form.instance.monto

        # Si el saldo es menor que 0, establecerlo en 0
        venta.saldo = max(venta.saldo, 0)
        print("Saldo antes:", venta.saldo)
        venta.save()
        print("Saldo despues:", venta.saldo)
        # Mensaje de éxito
        messages.success(self.request, 'Pago creado exitosamente.')

        return response
class PagoUpdateView(UpdateView):
    template_name = 'reservas/pago_update.html'
    # Si quieres editar todos los campos del form usa este codigo:
    form_class = PagoForm
    # Para editar solo campos especificos usa fields
    # fields = ['nombrec','telefenoc','usuarioc','passwordc','edadc','localidad']
    model = Pago
    success_url = reverse_lazy('pagos')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Pago modificado exitosamente.')
        return response


class PagoDeleteView(DeleteView):
    model = Pago  # Corregir aquí
    template_name = 'reservas/pago_confirm_delete.html'
    success_url = reverse_lazy('pagos')
    context_object_name = 'pago'  # También aquí

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Pago eliminado exitosamente.')
        return response


