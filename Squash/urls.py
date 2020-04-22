from django.urls import path
from Squash.views import IntegrantesqView, IntegrantesqInsertar, IntegrantesqEditar, IntegrantesqEliminar

urlpatterns = [
    path('Squash', IntegrantesqView.as_view(), name='integrantesq_list'),
    path('Squash/new',IntegrantesqInsertar.as_view(),name='insertar_integrantesq'),
    path('Squash/edit/<int:pk>',IntegrantesqEditar.as_view(),name='editar_integrantesq'),
    path('Squash/delete/<int:pk>',IntegrantesqEliminar.as_view(),name='borrar_integrantesq'),
]