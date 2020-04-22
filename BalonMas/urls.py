from django.urls import path
from BalonMas.views import IntegranteBView, IntegranteBInsertar, IntegranteBEditar, IntegranteBEliminar

urlpatterns = [
    path('BalonMas', IntegranteBView.as_view(), name='integranteb_list'),
    path('BalonMas/new',IntegranteBInsertar.as_view(),name='insertar_integranteb'),
    path('BalonMas/edit/<int:pk>',IntegranteBEditar.as_view(),name='editar_integranteb'),
    path('BalonMas/delete/<int:pk>',IntegranteBEliminar.as_view(),name='borrar_integranteb'),
]