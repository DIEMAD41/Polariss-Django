from . import views
from django.urls import path

urlpatterns = [
path('ReservacionesVuelos/', views.ReservacionVListView.as_view(), name='reservacionesV'),
path('ReservacionesVuelos/list/', views.ReservacionVAllListView.as_view(), name='reservacionesV_list'),
path('Reservaciones-new', views.ReservacionVCreateView.as_view(), name='reservacionesV_new'),

]