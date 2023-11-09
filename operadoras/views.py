from django.shortcuts import render
from operadoras.models import Operadoras

# Create your views here.
def listar_operadoras(request):
    operadoras = Operadoras.objects.all()
    data  = {
        'operadoras': operadoras
    }
    #Consulta a la BD seria como un SELECT * FROM Categoria
    return render(request,'operadoras_list.html',data)