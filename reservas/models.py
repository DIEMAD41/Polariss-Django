from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class ReservaVuelo(models.Model):
    CLASE = (
        ("PC", "Primera Clase"),
        ("CT", "Clase Turista"),
    )

    EQUIPAJE = (
        ("1", "Equipaje de Mano"),
        ("2", "Equipaje Documentado (25kg)"),
    )

    ESTADO = (
        ("P", "Pagado"),
        ("EP", "En Pago"),
        ("NP", "No pagado"),
    )

    clavev = models.AutoField(primary_key=True, blank=False, null=False)
    destinov = models.CharField(max_length=100, help_text="Destino del vuelo")
    origenv = models.CharField(max_length=100, help_text="Origen del vuelo")
    fsalida = models.DateField(help_text="Fecha de salida")
    fregreso = models.DateField(help_text="Fecha de regreso")
    npasajerosv = models.IntegerField(help_text="Número de pasajeros")
    tarifav = models.DecimalField(max_digits=20, decimal_places=2, help_text="Tarifa del vuelo")
    aerolinea = models.CharField(max_length=50, help_text="Aerolínea")
    comisionv = models.DecimalField(max_digits=10, decimal_places=2, help_text="Comisión de la reserva")
    clase = models.CharField(max_length=20, choices=CLASE, default="Clase Economica", help_text="Clase del vuelo")
    equipaje = models.CharField(max_length=50, choices=EQUIPAJE, default="Equipaje de Mano", help_text="Equipaje Documentado")
    estado = models.CharField(max_length=20, choices=ESTADO, default="NP", help_text="Estado de la reserva del vuelo")
    precio = models.DecimalField(max_digits=20, decimal_places=2, help_text="Precio de la reserva")  # Campo de precio
    clientes = models.ManyToManyField('clientes.Cliente', help_text="Clientes del vuelo")

    def __str__(self):
        return f"Reserva {self.clavev} - {self.destinov}"


class Venta(models.Model):
    ESTADO_VENTA = (
        ("NP", "No pagado"),
        ("P", "Pagado")

    )

    TIPO_VENTA = (
        ("Tarjeta", "Pago con Tarjeta"),
        ("Efectivo", "Pago en Efectivo"),
    )

    claveV = models.AutoField(primary_key=True, blank=False, null=False)
    fechaV = models.DateField(help_text="Fecha de la venta")
    total = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total de la venta")
    estado = models.CharField(max_length=10, choices=ESTADO_VENTA, default="No Pagado", help_text="Estado de la venta")
    reserva = models.ForeignKey(ReservaVuelo, on_delete=models.CASCADE, related_name='venta', help_text="Reserva asociada a la venta")
    saldo = models.DecimalField(max_digits=10, decimal_places=2, help_text="Saldo de la venta", null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calcula el total solo si es una venta nueva y el campo total no ha sido modificado manualmente
        if not self.pk and not self.total:
            self.total = self.reserva.precio
            self.saldo = self.total
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta {self.claveV} - Total: {self.total}"



class Pago(models.Model):
    METODOS_DE_PAGO = (
        ("Tarjeta", "Tarjeta"),
        ("Efectivo", "Efectivo"),
        # Agrega otros métodos de pago según sea necesario
    )


    fecha = models.DateField(help_text="Fecha del pago")
    metodo = models.CharField(max_length=20, choices=METODOS_DE_PAGO, help_text="Método de pago")
    monto = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monto del pago")
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='pagos', help_text="Venta asociada al pago")

    def __str__(self):
        return f"Pago - Venta: {self.venta.claveV}, Monto: {self.monto}"
