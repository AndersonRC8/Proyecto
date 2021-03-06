# Generated by Django 3.0.5 on 2020-04-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntegranteF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.BigIntegerField(max_length=100, unique=True)),
                ('programa', models.CharField(max_length=100)),
                ('condicion', models.CharField(max_length=100)),
                ('telefono', models.BigIntegerField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('nombreequipo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Integrantes',
            },
        ),
    ]
