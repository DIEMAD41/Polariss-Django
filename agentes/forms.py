from django import forms
from .models import Agentes

class AgenteForm(forms.ModelForm):
    class Meta:
        model = Agentes
        #Seleccionar los campos que queramos mostrar en el formulario
        #fields = ['clave','nombre','descripcion','descuento','estado']
        fields = '__all__'