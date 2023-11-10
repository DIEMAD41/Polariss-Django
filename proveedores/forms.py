from django import forms
from proveedores.models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        # Seleccionar los campos que querramos mostrar en el formulario
        model = Proveedor
        fields = '__all__'