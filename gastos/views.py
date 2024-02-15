from datetime import datetime

from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib import messages
from gastos.forms import GastosForm
from gastos.models import Gasto
from django.utils import timezone


# Create your views here.

#VISTAS BASADAS EN CLASES PARA RESERVACIONES DE VUELOS
class GastosListView(ListView):
    template_name = 'gastos/gastos_list.html'
    model = Gasto
    context_object_name = "gastos"
    paginate_by = 10

    def get_queryset(self):
        queryset = Gasto.objects.all()

        # Obtener parámetros de filtrado
        categoria = self.request.GET.get('categoria')
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')
        metodo_pago = self.request.GET.get('metodo_pago')

        # Aplicar filtros si se proporcionan
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        if fecha_inicio:
            queryset = queryset.filter(fecha__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha__lte=fecha_fin)
        if metodo_pago:
            queryset = queryset.filter(metodo_pago=metodo_pago)

        return queryset

class GastosCreateView(CreateView):
    template_name = 'gastos/gastos_new.html'
    form_class = GastosForm
    success_url = reverse_lazy('gastos')



    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Reserva creada exitosamente.')
        return response


class GastosUpdateView(UpdateView):
    template_name = 'gastos/gastos_update.html'
    form_class = GastosForm
    model = Gasto

    def get_success_url(self):
        return reverse_lazy('gastos')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Gasto modificado exitosamente.')
        return response

class GastosDeleteView(DeleteView):
    model =Gasto
    template_name = 'gastos/gastos_confirm_delete.html'
    success_url = reverse_lazy('gastos_deletes')
    context_object_name = 'gastos'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Gasto eliminado exitosamente.')
        return response

class GastosHomeView(TemplateView):
    template_name = 'gastos/gastos_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener los últimos diez gastos más recientes
        context['ultimos_diez_gastos'] = Gasto.objects.all().order_by('-fecha')[:10]

        # Obtener el mes y año seleccionados (por ejemplo, a través de un formulario)
        mes_anio_seleccionado_str = self.request.GET.get('mes', timezone.now().strftime('%Y-%m'))
        mes_anio_seleccionado = datetime.strptime(mes_anio_seleccionado_str, '%Y-%m')

        # Obtener los gastos del mes y año seleccionados
        gastos_mes_seleccionado = Gasto.objects.filter(fecha__year=mes_anio_seleccionado.year, fecha__month=mes_anio_seleccionado.month)

        # Calcular la suma total de los gastos del mes seleccionado
        total_mes_seleccionado = gastos_mes_seleccionado.aggregate(Sum('monto'))['monto__sum']
        context['total_mes_seleccionado'] = total_mes_seleccionado if total_mes_seleccionado is not None else 0

        # Agregar mes y año al contexto
        context['mes_anio_seleccionado'] = mes_anio_seleccionado

        # Obtener el año seleccionado (por ejemplo, a través de un formulario)
        anio_seleccionado = self.request.GET.get('anio', timezone.now().year)

        # Obtener los gastos del año seleccionado
        gastos_anio_seleccionado = Gasto.objects.filter(fecha__year=anio_seleccionado)

        # Calcular la suma total de los gastos del año seleccionado
        total_anio_seleccionado = gastos_anio_seleccionado.aggregate(Sum('monto'))['monto__sum']
        context['total_anio_seleccionado'] = total_anio_seleccionado if total_anio_seleccionado is not None else 0

        return context