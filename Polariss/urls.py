"""
URL configuration for Polariss project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gestion.urls')),
    path('',include('clientes.urls')),
    path('',include('proveedores.urls')),
    path('',include('operadoras.urls')),
    path('',include('agentes.urls')),
    path('clientes/',include(('clientes.urls','clientes'),namespace='clientes')),
    path('agentes/', include(('agentes.urls', 'agentes'), namespace='agentes')),
    path('proveedores/',include(('proveedores.urls','proveedores'),namespace='proveedores')),
    path('operadoras/',include(('operadoras.urls','operadoras'),namespace='operadoras')),

    #Reservas
    path('',include('reservas.urls')),
    path('reservas/',include(('reservas.urls','reservas'),namespace='reservas')),

    #Paquetes
    path('',include('paquetes.urls')),
    path('paquetes/',include(('paquetes.urls','paquetes'),namespace='paquetes')),
    #Paquete Api
    path('', include('paquetes.urls')),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
