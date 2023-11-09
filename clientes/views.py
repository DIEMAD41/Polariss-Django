from django.shortcuts import render
from clientes.models import Cliente

# Create your views here.
def clientes(request):
    data = {
        'clientes': clientes
    }
    response = render(request, 'clientes/clientes.html', context=data)
    response['X-Frame-Options'] = 'ALLOW-FROM *'
    return response
