# Generated by Django 2.2.1 on 2019-08-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('externo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimientoexterno',
            name='Horas',
            field=models.PositiveSmallIntegerField(verbose_name='Horas Fuera de Servicio'),
        ),
    ]