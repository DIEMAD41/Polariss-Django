from . import views
from django.urls import path

urlpatterns = [
#URLS DE PAGO
path('Gastos/', views.GastosListView.as_view(), name='gastos'),
path('Gastos/new/', views.GastosCreateView.as_view(), name='gastos_new'),
path('Gastos/<pk>/eliminar', views.GastosDeleteView.as_view(), name='gastos_delete'),
path('Gastos/update/<pk>', views.GastosUpdateView.as_view(), name='gastos_update'),

# Nueva ruta para la página principal de gastos
path('Gastos/home/', views.GastosHomeView.as_view(), name='gastos_home'),
]
