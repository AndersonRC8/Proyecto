from django.db import models

# Create your models here.
class IntegranteBF(models.Model):
    nombrebf=models.CharField(
        max_length=100,
        
    )
    cedulabf=models.BigIntegerField(
        max_length=100,
        unique=True
     )
    programabf=models.CharField(
        max_length=100,
    )
    condicionbf=models.CharField(
        max_length=100,
        
    )
    telefonobf=models.BigIntegerField(
        max_length=100,
        
    )
    emailbf=models.CharField(
        max_length=100,
        
    )
    nombreequipobf=models.CharField(
        max_length=100,
       
    )

    def __str__(self):
        return '{}'.format(self.nombreb)
    
    def save(self):
        self.parteconseguida = self.nombrebf.upper()
        super(IntegranteBF, self).save()
    
    class Meta:
        verbose_name_plural="Integrantes"
