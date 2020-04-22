from django import forms
from BalonFem.models import IntegranteBF

class IntegranteBFForm(forms.ModelForm):
    class Meta:
        model=IntegranteBF
        fields=['id','cedulabf','nombrebf','programabf','condicionbf','telefonobf','emailbf','nombreequipobf']
        labels={'cedulabf':"numero de cedula",'nombrebf':"Nombre del integrante",'programabf':"Carrera que estudia",'condicionbf':"Estudiante, profesor, tecnico",'telefonobf':"Telefono de integrante",'emailbf':"Email del integrante",'nombreequipobf':"Nombre del equipo"}
        widget={'cedulabf':forms.IntegerField,'nombrebf':forms.TextInput,'programabf':forms.TextInput,'condicionbf':forms.TextInput,'telefonobf':forms.IntegerField,'emailbf':forms.EmailInput}
