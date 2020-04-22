from django import forms
from Voleibol.models import IntegranteV

class IntegranteVForm(forms.ModelForm):
    class Meta:
        model=IntegranteV
        fields=['id','cedulav','nombrev','programav','condicionv','telefonov','emailv','nombreequipov']
        labels={'cedulav':"numero de cedula",'nombrev':"Nombre del integrante",'programav':"Carrera que estudia",'condicionv':"Condicion en la que se encuentra",'telefonov':"telefono de integrante",'emailv':"Email del integrante",'nombreequipov':"nombre del equipo"}
        widget={'cedulav':forms.IntegerField,'nombrev':forms.TextInput,'programav':forms.TextInput,'condicionv':forms.TextInput,'telefonov':forms.IntegerField,'emailv':forms.EmailInput}