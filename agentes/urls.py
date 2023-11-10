from django.urls import path
from . import views

urlpatterns = [
    path('lista_agendas/',views.listar_Agentes,name='agentes_list'),
    path('agregar_agente/', views.agregar_agente, name = 'agentes_new'),
    
]