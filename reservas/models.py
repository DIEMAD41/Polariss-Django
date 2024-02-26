from django.db import models

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
        ("EP", "En Pago"),
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
    equipaje = models.CharField(max_length=50, choices=EQUIPAJE, default="Equipaje de Mano", help_text="Equipaje permitido")
    estado = models.CharField(max_length=10, choices=ESTADO, default="No Pagado", help_text="Estado de la reserva del vuelo")
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio de la reserva")  # Campo de precio
    clientes = models.ManyToManyField('clientes.Cliente', help_text="Clientes del vuelo")

    def __str__(self):
        return f"Reserva {self.clavev} - {self.destinov}"


class Venta(models.Model):
    ESTADO_VENTA = (
        ("P", "Pagado"),
        ("NP", "No pagado"),
    )

    TIPO_VENTA = (
        ("Tarjeta", "Pago con Tarjeta"),
        ("Efectivo", "Pago en Efectivo"),
    )

    claveV = models.AutoField(primary_key=True, blank=False, null=False)
    fechaV = models.DateField(help_text="Fecha de la venta")
    total = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total de la venta")
    estado = models.CharField(max_length=10, choices=ESTADO_VENTA, default="No Pagado", help_text="Estado de la venta")
    tipo = models.CharField(max_length=20, choices=TIPO_VENTA, default="Efectivo", help_text="Tipo de pago")
    reservas = models.ManyToManyField(ReservaVuelo, related_name='ventas', help_text="Reservas asociadas a la venta")
    saldo = models.DecimalField(max_digits=10, decimal_places=2, help_text="Saldo de la venta", null=True, blank=True)

    def __str__(self):
        return f"Venta {self.claveV} - Total: {self.total}"

    def save(self, *args, **kwargs):
        # Si el saldo no se ha establecido, establecerlo como el total por defecto
        if not self.saldo:
            self.saldo = self.total
        else:
            # Ajustar el saldo si el total ha cambiado
            diferencia_total = self.total - self.saldo
            self.saldo += diferencia_total
        super().save(*args, **kwargs)  # Llamada al método save una vez, no dos veces


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
