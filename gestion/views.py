from django.shortcuts import render

from django.shortcuts import render


# Create your views here.
def home(request):
    data = {
        'titulo': 'Pagina Inicio',
        'nombre': 'Jose Isaias Alvarado Hernandez',
        'profesion': 'Ingeniero en Sistemas Computacionales',
        'lenguajes': ['JavaScript', 'Scratch', 'Assembler', 'PSEInt', 'SQL']
    }
    return render(request, 'gestion/index.html', context=data)


def register(request):
    data = {
        'titulo': 'Register'
    }
    return render(request, 'gestion/register.html', context=data)


def dashboard(request):
    data = {
        'titulo': 'Dashboard'
    }
    response = render(request, 'gestion/principal.html', context=data)
    response['X-Frame-Options'] = 'ALLOW-FROM *'
    return response

