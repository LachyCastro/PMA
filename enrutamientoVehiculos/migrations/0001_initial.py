# Generated by Django 3.2.7 on 2022-12-20 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('path', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('problem', models.CharField(max_length=200)),
                ('solutions_method', models.CharField(max_length=200)),
            ],
        ),
    ]
