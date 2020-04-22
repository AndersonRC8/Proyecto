from django.db import models

# Create your models here.
class IntegranteA(models.Model):
    nombrea=models.CharField(
        max_length=100,
        
    )
    cedulaa=models.BigIntegerField(
        max_length=100,
        unique=True
     )
    programaa=models.CharField(
        max_length=100,
    )
    condiciona=models.CharField(
        max_length=100,
        
    )
    telefonoa=models.BigIntegerField(
        max_length=100,
        
    )
    emaila=models.CharField(
        max_length=100,
        
    )
    dificultada=models.CharField(
        max_length=100,
       
    )

    def __str__(self):
        return '{}'.format(self.nombrea)
    
    def save(self):
        self.parteconseguida = self.nombrea.upper()
        super(IntegranteA, self).save()
    
    class Meta:
        verbose_name_plural='Integrantes'