
from . import views
from django.urls import path

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),  # http://127.0.01:8000/dashboard
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('obtener_datos_cliente/<int:cliente_id>/', views.obtener_datos_cliente, name='obtener_datos_cliente'),
    path('modificar_cliente/<int:cliente_id>/', views.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/', views.eliminar_cliente, name='eliminar_cliente'),

    #Basadas en clases urls
    path('clientes-list', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes-new', views.ClienteCreateView.as_view(), name='cliente_new'),
    path('clientes-update/<pk>', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('<pk>/eliminar', views.ClienteDeleteView.as_view(), name='eliminar_cliente'),


]
