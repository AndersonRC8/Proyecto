from django import forms
from FutsalMas.models import Integrante

class IntegranteForm(forms.ModelForm):
    class Meta:
        model=Integrante
        fields=['id','cedula','nombre','programa','condicion','telefono','email','nombreequipo']
        labels={'Cedula':"numero de cedula",'Nombres':"Nombre del integrante",'Programa':"Carrera que estudia",'condicion':"Condicion en la que se encuentra",'telefono':"telefono de integrante",'e-mail':"Email del integrante",'nombreequipo':"nombre del equipo"}
        widget={'cedula':forms.IntegerField,'nombre':forms.TextInput,'programa':forms.TextInput,'condicion':forms.TextInput,'telefono':forms.IntegerField,'email':forms.EmailInput}