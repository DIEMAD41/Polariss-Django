from django.db import models

# Create your models here.
class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombrec = models.CharField(max_length=255, blank=False, null=False)
    telefenoc = models.CharField(max_length=20)
    usuarioc = models.CharField(max_length=50, unique=True, blank=False, null=False)
    passwordc = models.CharField(max_length=100, blank=False, null=False)
    edadc = models.IntegerField()
    localidad = models.CharField(max_length=100)
    #En caso de que sea una relacion de muchos a muchos se usa este codigo, en este caso no
    #vuelos = models.ManyToManyField('reservas.ReservaVuelo', related_name='clientes')
    imagensrc = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombrec