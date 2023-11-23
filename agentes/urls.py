from django.urls import path
from . import views

urlpatterns = [
    path('agentes/', views.agentes, name='agentes'),  # http://127.0.01:8000/dashboard
    path('agregar_agente/', views.agregar_agente, name='agregar_agente'),
    path('obtener_datos_agente/<int:agente_id>/', views.obtener_datos_agente, name='obtener_datos_agente'),
    path('modificar_agente/<int:agente_id>/', views.modificar_agente, name='modificar_agente'),
    path('eliminar_agente/', views.eliminar_agente, name='eliminar_agente'),
    
]