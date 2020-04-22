from django.urls import path 
from Informacion.views import InformacionDeportes

urlpatterns=[
    path('Informacion', InformacionDeportes.as_view(), name='informacion_deportes'),
    ]