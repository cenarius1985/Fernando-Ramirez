# Generated by Django 2.2.1 on 2019-08-26 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0004_auto_20190825_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoreo',
            name='nombre1',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]