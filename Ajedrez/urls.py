from django.urls import path
from Ajedrez.views import IntegranteAView, IntegranteAInsertar, IntegranteAEditar, IntegranteAEliminar

urlpatterns = [
    path('Ajedrez', IntegranteAView.as_view(), name='integrantea_list'),
    path('Ajedrez/new',IntegranteAInsertar.as_view(),name='insertar_integrantea'),
    path('Ajedrez/edit/<int:pk>',IntegranteAEditar.as_view(),name='editar_integrantea'),
    path('Ajedrez/delete/<int:pk>',IntegranteAEliminar.as_view(),name='borrar_integrantea'),
]