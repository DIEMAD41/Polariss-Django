
from . import views
from django.urls import path

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),  # http://127.0.01:8000/dashboard
]
