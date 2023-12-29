from django import forms
from .models import Paquetes

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquetes
        #Campos que no quieres que se muestren
        exclude = ['idpaquete']
        #Seleccionar los campos que queramos mostrar en el formulario
        #fields = ['clave','nombre','descripcion','descuento','estado']
        fields = '__all__'
        #Etiquetas de los cambios
        labels = {
            'nombrep': 'Nombre del paquete',
            'descripcion': 'Descripción del paquete',
            'urlimagen': 'URL de la imagen',
            'costopersona':'Costo X Persona',
        }