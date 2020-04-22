from django.db import models

# Create your models here.
class IntegranteSq(models.Model):
    nombresq=models.CharField(
        max_length=100,
        
    )
    cedulasq=models.BigIntegerField(
        max_length=100,
        unique=True
     )
    programasq=models.CharField(
        max_length=100,
    )
    condicionsq=models.CharField(
        max_length=100,
        
    )
    telefonosq=models.BigIntegerField(
        max_length=100,
        
    )
    emailsq=models.CharField(
        max_length=100,
        
    )
    dificultadsq=models.CharField(
        max_length=100,
       
    )

    def __str__(self):
        return '{}'.format(self.nombresq)
    
    def save(self):
        self.parteconseguida = self.nombresq.upper()
        super(IntegranteSq, self).save()
    
    class Meta:
        verbose_name_plural='Integrantes'