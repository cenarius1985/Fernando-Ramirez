# Generated by Django 2.2.6 on 2019-11-01 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191101_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='x',
            field=models.IntegerField(),
        ),
    ]