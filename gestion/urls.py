
from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),  # http://127.0.01:8000/register
    path('', views.dashboard, name='dashboard'),  # http://127.0.01:8000/dashboard
]
