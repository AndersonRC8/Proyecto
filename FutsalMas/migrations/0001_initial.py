# Generated by Django 3.0.5 on 2020-04-17 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('cedula', models.BigIntegerField(max_length=100, unique=True)),
                ('programa', models.CharField(max_length=100, unique=True)),
                ('condicion', models.CharField(max_length=100, unique=True)),
                ('telefono', models.BigIntegerField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Integrantes',
            },
        ),
    ]