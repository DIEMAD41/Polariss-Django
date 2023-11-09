
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),  # Raiz o home http://127.0.01:8000/
    path('register/', views.register, name='register'),  # http://127.0.01:8000/register
    path('dashboard/', views.dashboard, name='dashboard'),  # http://127.0.01:8000/dashboard
]
