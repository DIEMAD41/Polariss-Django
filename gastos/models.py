from django.db import models
class Gasto(models.Model):
    CATEGORIA_CHOICES = [
        ('papeleria', 'Papelería'),
        ('mensuales', 'Gastos Mensuales'),
        ('otros', 'Otros'),
    ]

    nombre = models.CharField(max_length=20, blank=False)
    fecha = models.DateField()
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    recibo = models.ImageField(upload_to='recibos/', blank=True, null=True)

    def __str__(self):
        return f"{self.descripcion} - {self.monto} - {self.fecha}"
