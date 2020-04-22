"""Deportes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 



urlpatterns = [
    path('',include(('homeapp.urls','homeapp'),namespace='home')),
    path('Torneos/',include(('Torneos.urls','Torneos'),namespace='Torneos')),
    path('Informacion/',include(('Informacion.urls','Informacion'),namespace='Informacion')),
    path('Equipo/',include(('Equipo.urls','Equipo'),namespace='Equipo')),
    path('FutsalMas/',include(('FutsalMas.urls','FutsalMas'),namespace='FutsalMas')),
    path('FutsalFem/',include(('FutsalFem.urls','FutsalFem'),namespace='FutsalFem')),
    path('BalonMas/',include(('BalonMas.urls','BalonMas'),namespace='BalonMas')),
    path('BalonFem/',include(('BalonFem.urls','BalonFem'),namespace='BalonFem')),
    path('Voleibol/',include(('Voleibol.urls','Voleibol'),namespace='Voleibol')),
    path('Squash/',include(('Squash.urls','Squash'),namespace='Squash')),
    path('Ajedrez/',include(('Ajedrez.urls','Ajedrez'),namespace='Ajedrez')),
    path('admin/', admin.site.urls),
]

