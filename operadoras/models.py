from django.db import models

# Create your models here.

class Operadoras(models.Model):
    clave = models.PositiveIntegerField(unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50,unique=True,blank=False,null=False)
    email = models.EmailField(blank=True,null=True)
    #imagen = models.ImageField()

    def _str_(self):
        return self.nombre