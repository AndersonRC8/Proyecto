from django.urls import path
from BalonFem.views import IntegranteBFView, IntegranteBFInsertar, IntegranteBFEditar, IntegranteBFEliminar

urlpatterns = [
    path('BalonFem', IntegranteBFView.as_view(), name='integrantebf_list'),
    path('BalonFem/new',IntegranteBFInsertar.as_view(),name='insertar_integrantebf'),
    path('BalonFem/edit/<int:pk>',IntegranteBFEditar.as_view(),name='editar_integrantebf'),
    path('BalonFem/delete/<int:pk>',IntegranteBFEliminar.as_view(),name='borrar_integrantebf'),
]