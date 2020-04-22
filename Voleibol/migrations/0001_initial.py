# Generated by Django 3.0.5 on 2020-04-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntegranteV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrev', models.CharField(max_length=100)),
                ('cedulav', models.BigIntegerField(max_length=100, unique=True)),
                ('programav', models.CharField(max_length=100)),
                ('condicionv', models.CharField(max_length=100)),
                ('telefonov', models.BigIntegerField(max_length=100)),
                ('emailv', models.CharField(max_length=100)),
                ('nombreequipov', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Integrantes',
            },
        ),
    ]