from django.db import models


# Create your models here.
class ReservaVuelo(models.Model):
    CLASE = (
        ("PC", "Primera Clase"),
        ("CE", "Clase Ejecutiva"),
        ("E", "Clase Economica"),
    )

    EQUIPAJE = (
        ("1", "Equipaje de Mano"),
        ("2", "Equipaje Documentado (25kg)"),
    )

    ESTADO = (
        ("P", "Pagado"),
        ("NP", "No pagado"),
    )

    clavev = models.AutoField(primary_key=True, blank=False, null=False)
    destinov = models.CharField(max_length=100, help_text="Destino del vuelo")
    origenv = models.CharField(max_length=100, help_text="Origen del vuelo")
    fsalida = models.DateField(help_text="Fecha de salida")
    fregreso = models.DateField(help_text="Fecha de regreso")
    npasajerosv = models.IntegerField(help_text="Número de pasajeros")
    tarifav = models.DecimalField(max_digits=10, decimal_places=2, help_text="Tarifa del vuelo")
    aerolinea = models.CharField(max_length=50, help_text="Aerolínea")
    comisionv = models.DecimalField(max_digits=5, decimal_places=2, help_text="Comisión de la reserva")
    clase = models.CharField(max_length=10, choices=CLASE, default="Clase Economica", help_text="Clase del vuelo")
    equipaje = models.CharField(max_length=50, choices=EQUIPAJE, default="Equipaje de Mano",help_text="Equipaje permitido")
    estado = models.CharField(max_length=10, choices=ESTADO, default="No Pagado", help_text="Estado de la reserva del vuelo")
    # Clave foranea del cliente
    clientes = models.ManyToManyField('clientes.Cliente',help_text="Clientes del vuelo")

    def __str__(self):
        return f"Reserva {self.clavev} - {self.destinov}"