# Generated by Django 4.2.6 on 2023-11-10 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='nombreop',
            field=models.CharField(default='Operadora', max_length=255),
        ),
    ]
