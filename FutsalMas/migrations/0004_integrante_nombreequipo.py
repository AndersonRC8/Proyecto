# Generated by Django 3.0.5 on 2020-04-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FutsalMas', '0003_remove_integrante_nombreequipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrante',
            name='nombreequipo',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
