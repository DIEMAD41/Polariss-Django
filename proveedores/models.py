from django.db import models

# Create your models here.
class Proveedor(models.Model):
    idprov = models.AutoField(primary_key=True,unique=True, blank=False, null=False)
    nombreprov = models.CharField(max_length=255, blank=False, null=False)
    telefenoprov = models.CharField(max_length=20)
    correoprov = models.CharField(max_length=50, unique=True,blank=False, null=False)
    nombreop = models.CharField(max_length=255, blank=False, null=False,default='Operadora')
    
    def __str__(self):
        return self.nombreprov
