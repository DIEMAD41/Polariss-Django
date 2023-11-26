from django.db import models

# Create your models here.

class Operadoras(models.Model):
    clave = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, unique=True,blank=False,null=False)
    email = models.EmailField(blank=True, null=True)
    #imagen = models.ImageField()

    def __str__(self):
        return self.nombre