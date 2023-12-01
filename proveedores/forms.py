from django import forms
from proveedores.models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        # Seleccionar los campos que querramos mostrar en el formulario
        model = Proveedor
        
        #Campos que no quieres que se muestren
        exclude = ['idprov']
        # Campos que vas a mostrar
        fields = '__all__'
        #Etiquetas de los cambios
        labels = {
            'nombreprov': 'Nombre del proveedor',
            'telefenoprov': 'Telefono del proveedor',
            'correoprov': 'Correo',
            'nombreop': 'Operadora',
        }