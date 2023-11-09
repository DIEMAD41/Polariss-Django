from django import forms

from clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        # Seleccionar los campos que querramos mostrar en el formulario
        model = Cliente
        # fields = ['idcliente', 'nombrec', 'telefenoc', 'usuarioc', 'passwordc','edadc','localidad']
        fields = '__all__'