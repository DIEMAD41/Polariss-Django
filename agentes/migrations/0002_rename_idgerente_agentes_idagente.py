# Generated by Django 4.2.7 on 2023-11-10 03:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("agentes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="agentes",
            old_name="idgerente",
            new_name="idagente",
        ),
    ]
