from django.urls import path 
from Equipo.views import Equipo

urlpatterns=[
    path('Equipo', Equipo.as_view(), name='equipo'),
    ]