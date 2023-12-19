from django import forms
from .models import Operadoras

class OperadoraForm(forms.ModelForm):
    class Meta:
        model = Operadoras
        exclude = ['clave']
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la Operadora',
            'email': 'Email de la operadora',
        }

