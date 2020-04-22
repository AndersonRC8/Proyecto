from django import forms
from FutsalFem.models import IntegranteF

class IntegranteFForm(forms.ModelForm):
    class Meta:
        model=IntegranteF
        fields=['id','cedulaf','nombref','programaf','condicionf','telefonof','emailf','nombreequipof']
        labels={'cedulaf':"numero de cedula",'nombref':"Nombre del integrante",'programaf':"Carrera que estudia",'condicionf':"Estudiante, profesor, tecnico",'telefonof':"Telefono de integrante",'emailf':"Email del integrante",'nombreequipof':"Nombre del equipo"}
        widget={'cedulaf':forms.IntegerField,'nombref':forms.TextInput,'programaf':forms.TextInput,'condicionf':forms.TextInput,'telefonof':forms.IntegerField,'emailf':forms.EmailInput}
