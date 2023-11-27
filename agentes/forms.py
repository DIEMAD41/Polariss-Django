from django import forms
from .models import Agentes

class AgenteForm(forms.ModelForm):
    class Meta:
        model = Agentes
        #Campos que no quieres que se muestren
        exclude = ['idagente']
        #Seleccionar los campos que queramos mostrar en el formulario
        #fields = ['clave','nombre','descripcion','descuento','estado']
        fields = '__all__'
        #Etiquetas de los cambios
        labels = {
            'nombreg': 'Nombre del agente',
            'telefenog': 'Telefono del agente',
            'usuariog': 'Usuario',
            'passwordg': 'Contraseña',
            'saldo' : 'Saldo',
            'edadg': 'Edad del agente',
            'localidadg': 'Localidad',

        }