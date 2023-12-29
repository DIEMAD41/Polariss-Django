from django.db import models

# Create your models here.
class Paquetes(models.Model):
    idpaquete = models.AutoField(primary_key=True,unique=True, blank=False, null=False)
    nombrep = models.CharField(max_length=150, blank=False, null=False)
    descripcion = models.CharField(max_length=255,blank=True, null=True)
    urlimagen = models.CharField(max_length=255, unique=True,blank=False, null=False)
    costopersona = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True)

    def __str__(self):
        return self.nombrep