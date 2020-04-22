from django.urls import path
from FutsalMas.views import IntegranteView, IntegranteInsertar, IntegranteEditar, IntegranteEliminar

urlpatterns = [
    path('FutsalMas', IntegranteView.as_view(), name='integrante_list'),
    path('FutsalMas/new',IntegranteInsertar.as_view(),name='insertar_integrante'),
    path('FutsalMas/edit/<int:pk>',IntegranteEditar.as_view(),name='editar_integrante'),
    path('FutsalMas/delete/<int:pk>',IntegranteEliminar.as_view(),name='borrar_integrante'),
]