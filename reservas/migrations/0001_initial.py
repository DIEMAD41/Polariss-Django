# Generated by Django 5.0 on 2023-12-29 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_cliente_imagensrc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaVuelo',
            fields=[
                ('clavev', models.AutoField(primary_key=True, serialize=False)),
                ('destinov', models.CharField(help_text='Destino del vuelo', max_length=100)),
                ('origenv', models.CharField(help_text='Origen del vuelo', max_length=100)),
                ('fsalida', models.DateField(help_text='Fecha de salida')),
                ('fregreso', models.DateField(help_text='Fecha de regreso')),
                ('npasajerosv', models.IntegerField(help_text='Número de pasajeros')),
                ('tarifav', models.DecimalField(decimal_places=2, help_text='Tarifa del vuelo', max_digits=10)),
                ('aerolinea', models.CharField(help_text='Aerolínea', max_length=50)),
                ('comisionv', models.DecimalField(decimal_places=2, help_text='Comisión de la reserva', max_digits=5)),
                ('clase', models.CharField(choices=[('PC', 'Primera Clase'), ('CE', 'Clase Ejecutiva'), ('E', 'Clase Economica')], default='Clase Economica', help_text='Clase del vuelo', max_length=10)),
                ('equipaje', models.CharField(choices=[('1', 'Equipaje de Mano'), ('2', 'Equipaje Documentado (25kg)')], default='Equipaje de Mano', help_text='Equipaje permitido', max_length=50)),
                ('estado', models.CharField(choices=[('P', 'Pagado'), ('NP', 'No pagado')], default='No Pagado', help_text='Estado de la reserva del vuelo', max_length=10)),
                ('precio', models.DecimalField(decimal_places=2, help_text='Precio de la reserva', max_digits=10)),
                ('clientes', models.ManyToManyField(help_text='Clientes del vuelo', to='clientes.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('claveV', models.AutoField(primary_key=True, serialize=False)),
                ('fechaV', models.DateField(help_text='Fecha de la venta')),
                ('total', models.DecimalField(decimal_places=2, help_text='Total de la venta', max_digits=10)),
                ('estado', models.CharField(choices=[('P', 'Pagado'), ('NP', 'No pagado')], default='No Pagado', help_text='Estado de la venta', max_length=10)),
                ('tipo', models.CharField(choices=[('Tarjeta', 'Pago con Tarjeta'), ('Efectivo', 'Pago en Efectivo')], default='Efectivo', help_text='Tipo de pago', max_length=20)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, help_text='Saldo de la venta', max_digits=10)),
                ('reservas', models.ManyToManyField(help_text='Reservas asociadas a la venta', related_name='ventas', to='reservas.reservavuelo')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(help_text='Fecha del pago')),
                ('metodo', models.CharField(choices=[('Tarjeta', 'Tarjeta'), ('Efectivo', 'Efectivo')], help_text='Método de pago', max_length=20)),
                ('monto', models.DecimalField(decimal_places=2, help_text='Monto del pago', max_digits=10)),
                ('venta', models.ForeignKey(blank=True, help_text='Venta asociada al pago', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pagos', to='reservas.venta')),
            ],
        ),
    ]
