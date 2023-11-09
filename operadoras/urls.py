from django.urls import path
from . import views

urlpatterns = [
    path('lista_operadoras/',views.listar_operadoras,name='operadoras_list'),
]