from django.shortcuts import render

# Create your views here.
def clientes(request):
    data = {
        'titulo': 'Clientes'
    }
    response = render(request, 'clientes/clientes.html', context=data)
    response['X-Frame-Options'] = 'ALLOW-FROM *'
    return response
