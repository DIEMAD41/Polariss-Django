from django import forms

from clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        #Campos que no quieres que se muestren
        exclude = ['idcliente']
        # Campos que vas a mostrar
        fields = '__all__'
        #Etiquetas de los cambios
        labels = {
            'nombrec': 'Nombre del cliente',
            'telefenoc': 'Telefono del cliente',
            'usuarioc': 'Usuario',
            'passwordc': 'Contraseña',
            'edadc': 'Edad del cliente',
            'localidad': 'Localidad',

        }
