# Generated by Django 3.0.5 on 2020-04-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FutsalMas', '0005_auto_20200417_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrante',
            name='condicion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='nombreequipo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='telefono',
            field=models.BigIntegerField(max_length=100),
        ),
    ]