from django import forms
from Squash.models import IntegranteSq

class IntegranteSqForm(forms.ModelForm):
    class Meta:
        model=IntegranteSq
        fields=['id','cedulasq','nombresq','programasq','condicionsq','telefonosq','emailsq','dificultadsq']
        labels={'cedulasq':"numero de cedula",'nombresq':"Nombre del integrante",'programasq':"Carrera que estudia",'condicionsq':"Condicion en la que se encuentra",'telefonosq':"telefono de integrante",'emailsq':"Email del integrante",'dificultadsq':"Basico, intermedio, experto"}
        widget={'cedulasq':forms.IntegerField,'nombresq':forms.TextInput,'programasq':forms.TextInput,'condicionsq':forms.TextInput,'telefonosq':forms.IntegerField,'emailsq':forms.EmailInput,'dificultadsq':forms.TextInput}