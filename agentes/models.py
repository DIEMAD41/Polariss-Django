from django.db import models

# Create your models here.
class Agentes(models.Model):
    idagente = models.AutoField(primary_key=True,unique=True, blank=False, null=False)
    nombreg = models.CharField(max_length=255, blank=False, null=False)
    telefenog = models.CharField(max_length=20)
    usuariog = models.CharField(max_length=50, unique=True,blank=False, null=False)
    passwordg = models.CharField(max_length=100,blank=False, null=False)
    saldo = models.IntegerField()
    edadg = models.IntegerField()
    localidadg = models.CharField(max_length=100)
    #imagen = models.ImageField()

    def __str__(self):
        return self.nombreg