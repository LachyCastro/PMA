# Generated by Django 3.2.7 on 2022-12-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrutamientoVehiculos', '0003_auto_20221220_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='autor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='solutions_method',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]