from django import forms
from django.forms.widgets import DateInput
from crispy_forms.helper import FormHelper

from gastos.models import Gasto
from reservas.models import Pago

class GastosForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}),
        }