from django.db import models

# Create your models here.
class Integrante(models.Model):
    nombre=models.CharField(
        max_length=100,
        
    )
    cedula=models.BigIntegerField(
        max_length=100,
        unique=True
     )
    programa=models.CharField(
        max_length=100,
    )
    condicion=models.CharField(
        max_length=100,
        
    )
    telefono=models.BigIntegerField(
        max_length=100,
        
    )
    email=models.CharField(
        max_length=100,
        
    )
    nombreequipo=models.CharField(
        max_length=100,
       
    )

    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.parteconseguida = self.nombre.upper()
        super(Integrante, self).save()
    
    class Meta:
        verbose_name_plural='Integrantes'