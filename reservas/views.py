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
from django.db.models import Prefetch


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
    template_name = 'reservas/reservasV_list.html'
    model = ReservaVuelo
    context_object_name = "reservas"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener los parámetros GET de la URL
        cliente = self.request.GET.get('cliente')
        origen = self.request.GET.get('origen')
        destino = self.request.GET.get('destino')
        fecha_ida_min = self.request.GET.get('fecha_ida_min')
        fecha_ida_max = self.request.GET.get('fecha_ida_max')
        fecha_regreso_min = self.request.GET.get('fecha_regreso_min')
        fecha_regreso_max = self.request.GET.get('fecha_regreso_max')
        aerolinea = self.request.GET.get('aerolinea')
        estado = self.request.GET.get('estado')

        # Aplicar filtros si los parámetros están presentes
        if cliente:
            queryset = queryset.filter(clientes__nombrec__icontains=cliente)
        if origen:
            queryset = queryset.filter(origenv__icontains=origen)
        if destino:
            queryset = queryset.filter(destinov__icontains=destino)
        if fecha_ida_min:
            queryset = queryset.filter(fsalida__gte=fecha_ida_min)
        if fecha_ida_max:
            queryset = queryset.filter(fsalida__lte=fecha_ida_max)
        if fecha_regreso_min:
            queryset = queryset.filter(fregreso__gte=fecha_regreso_min)
        if fecha_regreso_max:
            queryset = queryset.filter(fregreso__lte=fecha_regreso_max)
        if aerolinea:
            queryset = queryset.filter(aerolinea__icontains=aerolinea)
        if estado:
            queryset = queryset.filter(estado=estado)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasar los parámetros GET a la plantilla para mantener los filtros
        context['get_params'] = self.request.GET
        return context


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
    template_name = 'reservas/venta_list.html'
    model = Venta
    context_object_name = "ventas"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = super().get_queryset().prefetch_related('pagos')  # Prefetch para obtener los pagos asociados
        cliente = self.request.GET.get('cliente')
        fecha_min = self.request.GET.get('fecha_min')
        fecha_max = self.request.GET.get('fecha_max')
        tipo = self.request.GET.get('tipo')
        total_min = self.request.GET.get('total_min')
        total_max = self.request.GET.get('total_max')
        saldo_min = self.request.GET.get('saldo_min')
        saldo_max = self.request.GET.get('saldo_max')

        if cliente:
            queryset = queryset.filter(reservas__clientes__nombrec__icontains=cliente)
        if fecha_min:
            queryset = queryset.filter(fechaV__gte=fecha_min)
        if fecha_max:
            queryset = queryset.filter(fechaV__lte=fecha_max)
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        if total_min:
            queryset = queryset.filter(total__gte=total_min)
        if total_max:
            queryset = queryset.filter(total__lte=total_max)
        if saldo_min:
            queryset = queryset.filter(saldo__gte=saldo_min)
        if saldo_max:
            queryset = queryset.filter(saldo__lte=saldo_max)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_params'] = self.request.GET
        return context

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
#Punto de conexión
def obtener_pagos(request, claveV):
    # Obtener la venta correspondiente a la claveV proporcionada
    venta = Venta.objects.get(claveV=claveV)
    # Obtener todos los pagos relacionados a la venta y obtener sus datos de fecha, método y monto
    pagos = venta.pagos.all().values('fecha', 'metodo', 'monto')
    # Devolver los datos de los pagos como una respuesta JSON
    return JsonResponse({'pagos': list(pagos)})


#VIEWS DE PAGO
class PagosListView(ListView):
    template_name = 'reservas/pago_list.html'
    model = Pago
    context_object_name = "pagos"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        venta_nombre = self.request.GET.get('venta')
        fecha_min = self.request.GET.get('fecha_min')
        fecha_max = self.request.GET.get('fecha_max')
        metodo = self.request.GET.get('metodo')
        monto_min = self.request.GET.get('monto_min')
        monto_max = self.request.GET.get('monto_max')

        if venta_nombre:
            # Filtrar por el nombre de la venta utilizando el campo 'nombre' en el modelo relacionado
            queryset = queryset.filter(venta__nombre__icontains=venta_nombre)
        if fecha_min:
            queryset = queryset.filter(fecha__gte=fecha_min)
        if fecha_max:
            queryset = queryset.filter(fecha__lte=fecha_max)
        if metodo:
            queryset = queryset.filter(metodo=metodo)
        if monto_min:
            queryset = queryset.filter(monto__gte=monto_min)
        if monto_max:
            queryset = queryset.filter(monto__lte=monto_max)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['get_params'] = self.request.GET
        return context

class PagosCreateView(CreateView):
    template_name = 'reservas/pago_new.html'
    form_class = PagoForm
    success_url = reverse_lazy('ventas')

    def get_initial(self):
        initial = super().get_initial()
        venta_id = self.request.GET.get('venta')
        if venta_id:
            # Establece la venta inicial si se proporciona en los parámetros de la URL
            initial['venta'] = venta_id
        return initial

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


