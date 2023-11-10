from django.shortcuts import render, redirect
from agentes.models import Agentes
from agentes.forms import AgenteForm
from django.contrib import messages

# Create your views here.
def listar_Agentes(request):
    agentes = Agentes.objects.all()
    data  = {
        'agentes': agentes
    }
    #Consulta a la BD seria como un SELECT * FROM Operadoras
    return render(request,'agentes_list.html',data)


def agregar_agente(request):
    data = {
        'form' : AgenteForm()
    }
    # Verificar si el usuario ya presiono el boton de envio POST
    if request.method == 'POST':
        # Formulario con los datos eviados
        formulario = AgenteForm(data=request.POST)
        if formulario.is_valid(): # Solo con esto verifica si son coreectos
            formulario.save()
            messages.success(request, "Agente Agregado")
            data['mensaje'] = 'Agente Agregada'
            return redirect(to='agentes:agentes_list')
        else:
            data['form'] = formulario # Regresa el formulario con los errores

    return render(request, 'agentes_new.html', data)