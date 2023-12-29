from django.urls import path
from . import views

urlpatterns = [
    path('', views.paquetes, name='paquetes'),  # http://127.0.01:8000/dashboard
    #Basadas en clases urls
    path('paquetes-list', views.PaqueteListView.as_view(), name='paquetes_list'),
    path('paquetes-new', views.PaqueteCreateView.as_view(), name='paquetes_new'),
    path('paquetes-update/<pk>', views.PaqueteUpdateView.as_view(), name='paquetes_update'),
    path('<pk>/eliminar', views.PaqueteDeleteView.as_view(), name='eliminar_paquetes'),
    
]