from django import forms
from Ajedrez.models import IntegranteA

class IntegranteAForm(forms.ModelForm):
    class Meta:
        model=IntegranteA
        fields=['id','cedulaa','nombrea','programaa','condiciona','telefonoa','emaila','dificultada']
        labels={'cedulaa':"numero de cedula",'nombrea':"Nombre del integrante",'programaa':"Carrera que estudia",'condiciona':"Condicion en la que se encuentra",'telefonoa':"telefono de integrante",'emaila':"Email del integrante",'dificultada':"Basico, intermedio, experto"}
        widget={'cedulaa':forms.IntegerField,'nombrea':forms.TextInput,'programaa':forms.TextInput,'condiciona':forms.TextInput,'telefonoa':forms.IntegerField,'emaila':forms.EmailInput,'dificultada':forms.TextInput}