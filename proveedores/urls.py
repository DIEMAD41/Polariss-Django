
from . import views
from django.urls import path

urlpatterns = [
    path('proveedores/', views.proveedores, name='proveedores'),
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('obtener_datos_proveedor/<int:prov_id>/', views.obtener_datos_proveedor, name='obtener_datos_proveedor'),
    path('modificar_proveedor/<int:prov_id>/', views.modificar_proveedor, name='modificar_proveedor'),
    path('eliminar_proveedor/', views.eliminar_proveedor, name='eliminar_proveedor'),

    #Basadas en clases urls
    path('proveedores-list', views.ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores-new', views.ProveedorCreateView.as_view(), name='proveedor_new'),
    path('proveedores-update/<pk>', views.ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('<pk>/eliminar', views.ProveedorDeleteView.as_view(), name='eliminar_proveedor'),
]
