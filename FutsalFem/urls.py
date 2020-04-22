from django.urls import path
from FutsalFem.views import IntegranteFView, IntegranteFInsertar, IntegranteFEditar, IntegranteFEliminar

urlpatterns = [
    path('FutsalFem', IntegranteFView.as_view(), name='integrantef_list'),
    path('FutsalFem/new',IntegranteFInsertar.as_view(),name='insertar_integrantef'),
    path('FutsalFem/edit/<int:pk>',IntegranteFEditar.as_view(),name='editar_integrantef'),
    path('FutsalFem/delete/<int:pk>',IntegranteFEliminar.as_view(),name='borrar_integrantef'),
]