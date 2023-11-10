from django import forms
from .models import Operadoras

class OperadoraForm(forms.ModelForm):
    class Meta:
        model = Operadoras
        #Seleccionar los campos que queramos mostrar en el formulario
        #fields = ['clave','nombre','descripcion','descuento','estado']
        fields = '__all__'