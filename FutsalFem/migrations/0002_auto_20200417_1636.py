# Generated by Django 3.0.5 on 2020-04-17 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FutsalFem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='integrantef',
            old_name='cedula',
            new_name='cedulaf',
        ),
        migrations.RenameField(
            model_name='integrantef',
            old_name='condicion',
            new_name='condicionf',
        ),
        migrations.RenameField(
            model_name='integrantef',
            old_name='email',
            new_name='emailf',
        ),
        migrations.RenameField(
            model_name='integrantef',
            old_name='nombre',
            new_name='nombreequipof',
        ),
        migrations.RenameField(
            model_name='integrantef',
            old_name='nombreequipo',
            new_name='nombref',
        ),
        migrations.RenameField(
            model_name='integrantef',
            old_name='programa',
            new_name='programaf',
        ),
        migrations.RenameField(
            model_name='integrantef',
            old_name='telefono',
            new_name='telefonof',
        ),
    ]