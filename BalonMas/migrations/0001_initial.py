# Generated by Django 3.0.5 on 2020-04-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntegranteB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreb', models.CharField(max_length=100)),
                ('cedulab', models.BigIntegerField(max_length=100, unique=True)),
                ('programab', models.CharField(max_length=100)),
                ('condicionb', models.CharField(max_length=100)),
                ('telefonob', models.BigIntegerField(max_length=100)),
                ('emailb', models.CharField(max_length=100)),
                ('nombreequipob', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Integrantes',
            },
        ),
    ]
