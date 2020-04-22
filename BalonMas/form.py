from django import forms
from BalonMas.models import IntegranteB

class IntegranteBForm(forms.ModelForm):
    class Meta:
        model=IntegranteB
        fields=['id','cedulab','nombreb','programab','condicionb','telefonob','emailb','nombreequipob']
        labels={'cedulab':"numero de cedula",'nombreb':"Nombre del integrante",'programab':"Carrera que estudia",'condicionb':"Estudiante, profesor, tecnico",'telefonob':"Telefono de integrante",'emailb':"Email del integrante",'nombreequipob':"Nombre del equipo"}
        widget={'cedulab':forms.IntegerField,'nombreb':forms.TextInput,'programab':forms.TextInput,'condicionb':forms.TextInput,'telefonob':forms.IntegerField,'emailb':forms.EmailInput}
