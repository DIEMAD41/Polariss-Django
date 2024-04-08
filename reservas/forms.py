from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from reservas.models import ReservaVuelo, Venta, Pago


class ReservaVueloForm(forms.ModelForm):
    class Meta:
        model = ReservaVuelo
        #Campos que no quieres que se muestren
        exclude = ['clavev','estado']
        # Campos que vas a mostrar
        fields = '__all__'
        #Etiquetas de los cambios
        """
        labels = {
            'nombrec': 'Nombre del cliente',
            'npasajerosv':'Numero de pasajeros',
            'telefenoc': 'Telefono del cliente',
            'usuarioc': 'Usuario',
            'passwordc': 'Contraseña',
            'edadc': 'Edad del cliente',
            'localidad': 'Localidad',

        }"""

        helper = FormHelper()
        helper.form_method = 'post'
        helper.layout = Layout(
            Field('Destinov', css_class=''),
            Field('Origenv', css_class='otra-clase-personalizada'),
            # Otros campos...
            Submit('submit', 'Enviar', css_class='boton-personalizado')
        )



class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        exclude = ['saldo','total']
        fields = '__all__'
        widgets={
            'fechaV': forms.TextInput(attrs={'type': 'date'})
        }



class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }



