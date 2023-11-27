from django.urls import path
from . import views

urlpatterns = [
    path('operadoras/', views.operadoras, name='operadoras'),  # http://127.0.01:8000/dashboard
    path('agregar_operadora/', views.agregar_operadora, name='agregar_operadora'),
    path('obtener_datos_operadora/<int:clave>/', views.obtener_datos_operadora, name='obtener_datos_operadora'),
    path('modificar_operadora/<int:clave>/', views.modificar_operadora, name='modificar_operadora'),
    path('eliminar_operadora/', views.eliminar_operadora, name='eliminar_operadora'),

    #Basadas en clases urls
    path('operadoras-list', views.OperadoraListView.as_view(), name='operadoras_list'),
    path('operadora-new', views.OperadoraCreateView.as_view(), name='operadora_new'),
    path('operadora-update/<pk>', views.OperadoraUpdateView.as_view(), name='operadora_update'),
    path('<pk>/eliminar', views.OperadoraDeleteView.as_view(), name='eliminar_operadora'),

]