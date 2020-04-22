from django.db import models

# Create your models here.
class IntegranteF(models.Model):
    nombref=models.CharField(
        max_length=100,
        
    )
    cedulaf=models.BigIntegerField(
        max_length=100,
        unique=True
     )
    programaf=models.CharField(
        max_length=100,
    )
    condicionf=models.CharField(
        max_length=100,
        
    )
    telefonof=models.BigIntegerField(
        max_length=100,
        
    )
    emailf=models.CharField(
        max_length=100,
        
    )
    nombreequipof=models.CharField(
        max_length=100,
       
    )

    def __str__(self):
        return '{}'.format(self.nombref)
    
    def save(self):
        self.parteconseguida = self.nombref.upper()
        super(IntegranteF, self).save()
    
    class Meta:
        verbose_name_plural="Integrantes"
