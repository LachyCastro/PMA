# Generated by Django 3.2.7 on 2022-12-20 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrutamientoVehiculos', '0002_auto_20221220_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='autor',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='publication',
            name='solutions_method',
            field=models.CharField(default='', max_length=200),
        ),
    ]