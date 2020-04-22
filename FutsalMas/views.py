from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from FutsalMas.models import Integrante
from FutsalMas.form import IntegranteForm
from django.http import  HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IntegranteView(generic.ListView):
    model=Integrante
    template_name='integrante_list.html'
    context_object_name='obj'
class IntegranteInsertar(generic.CreateView):
    model=Integrante
    context_object_name="obj"
    template_name="insertar_integrante.html"
    form_class=IntegranteForm
    success_url=reverse_lazy('FutsalMas:integrante_list')
class IntegranteEditar(generic.UpdateView):
    model=Integrante
    context_object_name="obj"
    template_name="insertar_integrante.html"
    form_class=IntegranteForm
    success_url=reverse_lazy('FutsalMas:integrante_list')
class IntegranteEliminar(generic.DeleteView):
    model = Integrante
    template_name="integrante_borrar.html"
    context_object_name="obj"
    success_url=reverse_lazy("FutsalMas:integrante_list")