from . import views
from django.urls import path

urlpatterns = [
path('ReservacionesVuelos/', views.ReservacionVListView.as_view(), name='reservacionesV'),
path('ReservacionesVuelos/list/', views.ReservacionVAllListView.as_view(), name='reservacionesV_list'),
path('ReservacionesVuelos/new/', views.ReservacionVCreateView.as_view(), name='reservacionesV_new'),
path('update/<pk>', views.ReservacionUpdateView.as_view(), name='reservacionesV_update'),
path('<pk>/eliminar', views.ReservacionDeleteView.as_view(), name='reservacionesV_delete'),


#URLS DE VENTA
path('Ventas/', views.VentasVAllListView.as_view(), name='ventas'),
path('Ventas/new/', views.VentasCreateView.as_view(), name='ventas_new'),
path('Ventas/update/<pk>', views.VentasUpdateView.as_view(), name='ventas_update'),
path('Ventas/<pk>/eliminar', views.VentasDeleteView.as_view(), name='ventas_delete'),


#URLS DE PAGO
path('Pagos/', views.PagosListView.as_view(), name='pagos'),
path('Pagos/new/', views.PagosCreateView.as_view(), name='pagos_new'),
path('Pagos/<pk>/eliminar', views.PagoDeleteView.as_view(), name='pagos_delete'),
path('Pagos/update/<pk>', views.PagoUpdateView.as_view(), name='pagos_update'),

]