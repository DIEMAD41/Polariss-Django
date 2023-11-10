from django.urls import path
from . import views

urlpatterns = [
    path('lista_operadoras/',views.listar_operadoras,name='operadoras_list'),
    path('agregar_operadora/',views.agregar_operadora,name='operadoras_new'),
    path('actualizar_operadora/<id>/', views.actualizar_operadora, name='operadoras_update'),
    path('eliminar_operadora/<id>/', views.elimar_operadora, name='operadora_delete'),
]