from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from Voleibol.models import IntegranteV
from Voleibol.form import IntegranteVForm
from django.http import  HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IntegranteVView(generic.ListView):
    model=IntegranteV
    template_name='integrantev_list.html'
    context_object_name='obj'
class IntegranteVInsertar(generic.CreateView):
    model=IntegranteV
    context_object_name="obj"
    template_name="insertar_integrantev.html"
    form_class=IntegranteVForm
    success_url=reverse_lazy('Voleibol:integrantev_list')
class IntegranteVEditar(generic.UpdateView):
    model=IntegranteV
    context_object_name="obj"
    template_name="insertar_integrantev.html"
    form_class=IntegranteVForm
    success_url=reverse_lazy('Voleibol:integrantev_list')
class IntegranteVEliminar(generic.DeleteView):
    model = IntegranteV
    template_name="integrantev_borrar.html"
    context_object_name="obj"
    success_url=reverse_lazy("Voleibol:integrantev_list")