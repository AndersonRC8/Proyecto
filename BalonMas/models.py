from django.db import models

# Create your models here.
class IntegranteB(models.Model):
    nombreb=models.CharField(
        max_length=100,
        
    )
    cedulab=models.BigIntegerField(
        max_length=100,
        unique=True
     )
    programab=models.CharField(
        max_length=100,
    )
    condicionb=models.CharField(
        max_length=100,
        
    )
    telefonob=models.BigIntegerField(
        max_length=100,
        
    )
    emailb=models.CharField(
        max_length=100,
        
    )
    nombreequipob=models.CharField(
        max_length=100,
       
    )

    def __str__(self):
        return '{}'.format(self.nombreb)
    
    def save(self):
        self.parteconseguida = self.nombreb.upper()
        super(IntegranteB, self).save()
    
    class Meta:
        verbose_name_plural="Integrantes"
