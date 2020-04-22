from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from Squash.models import IntegranteSq
from Squash.form import IntegranteSqForm
from django.http import  HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IntegrantesqView(generic.ListView):
    model=IntegranteSq
    template_name='integrantesq_list.html'
    context_object_name='obj'
class IntegrantesqInsertar(generic.CreateView):
    model=IntegranteSq
    context_object_name="obj"
    template_name="insertar_integrantesq.html"
    form_class=IntegranteSqForm
    success_url=reverse_lazy('Squash:integrantesq_list')
class IntegrantesqEditar(generic.UpdateView):
    model=IntegranteSq
    context_object_name="obj"
    template_name="insertar_integrantesq.html"
    form_class=IntegranteSqForm
    success_url=reverse_lazy('Squash:integrantesq_list')
class IntegrantesqEliminar(generic.DeleteView):
    model = IntegranteSq
    template_name="integrantesq_borrar.html"
    context_object_name="obj"
    success_url=reverse_lazy("Squash:integrantesq_list")