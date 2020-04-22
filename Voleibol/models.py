from django.db import models

# Create your models here.
class IntegranteV(models.Model):
    nombrev=models.CharField(
        max_length=100,
        
    )
    cedulav=models.BigIntegerField(
        max_length=100,
        unique=True
     )
    programav=models.CharField(
        max_length=100,
    )
    condicionv=models.CharField(
        max_length=100,
        
    )
    telefonov=models.BigIntegerField(
        max_length=100,
        
    )
    emailv=models.CharField(
        max_length=100,
        
    )
    nombreequipov=models.CharField(
        max_length=100,
       
    )

    def __str__(self):
        return '{}'.format(self.nombrev)
    
    def save(self):
        self.parteconseguida = self.nombrev.upper()
        super(IntegranteV, self).save()
    
    class Meta:
        verbose_name_plural='Integrantes'