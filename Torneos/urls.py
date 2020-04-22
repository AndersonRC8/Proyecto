from django.urls import path 
from Torneos.views import Informacion

urlpatterns=[
    path('Torneos', Informacion.as_view(), name='informacion'),
    ]