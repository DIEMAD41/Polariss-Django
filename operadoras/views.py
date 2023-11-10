from django.shortcuts import render, get_object_or_404, redirect
from operadoras.models import Operadoras
from operadoras.forms import OperadoraForm
from django.contrib import messages

# Create your views here.
def listar_operadoras(request):
    operadoras = Operadoras.objects.all()
    data  = {
        'operadoras': operadoras
    }
    #Consulta a la BD seria como un SELECT * FROM Operadoras
    return render(request,'operadoras_list.html',data)

def agregar_operadora(request):
    data = {
        'form': OperadoraForm()
    }
    # Verificar si el usuario ya presiono el boton de envio POST
    if request.method == 'POST':
        # Formulario con los datos eviados
        formulario = OperadoraForm(data=request.POST)
        if formulario.is_valid(): # Solo con esto verifica si son coreectos
            formulario.save()
            messages.success(request, "Operadora Agregada")
            data['mensaje'] = 'Operadora Agregada'
            return redirect(to='operadoras:operadoras_list')
        else:
            data['form'] = formulario # Regresa el formulario con los errores

    return render(request, 'operadoras_new.html', data)

def actualizar_operadora(request, id):
    operadora = get_object_or_404(Operadoras, id=id)
    data ={
            'form':OperadoraForm(instance=operadora)
    }
        # Si el usuario ya dijo que si, POST
    if request.method == 'POST':
        formulario = OperadoraForm(data=request.POST, instance=operadora)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Operadora Actualizada")
            return redirect(to='operadoras:operadoras_list')
            # Si no es valido
        data['form'] = formulario
    return render(request, 'operadoras_update.html',data)

def elimar_operadora(request,id):
    operadora = get_object_or_404(Operadoras, id=id)
    operadora.delete()
    messages.success(request, "Operadora Eliminada")
    return redirect(to='operadoras:operadoras_list')