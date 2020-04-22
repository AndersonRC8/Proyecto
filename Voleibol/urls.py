from django.urls import path
from Voleibol.views import IntegranteVView, IntegranteVInsertar, IntegranteVEditar, IntegranteVEliminar

urlpatterns = [
    path('Voleibol', IntegranteVView.as_view(), name='integrantev_list'),
    path('Voleibol/new',IntegranteVInsertar.as_view(),name='insertar_integrantev'),
    path('Voleibol/edit/<int:pk>',IntegranteVEditar.as_view(),name='editar_integrantev'),
    path('Voleibol/delete/<int:pk>',IntegranteVEliminar.as_view(),name='borrar_integrantev'),
]