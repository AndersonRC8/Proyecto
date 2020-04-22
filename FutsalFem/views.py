from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from FutsalFem.models import IntegranteF
from FutsalFem.form import IntegranteFForm
from django.http import  HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IntegranteFView(generic.ListView):
    model=IntegranteF
    template_name='integrantef_list.html'
    context_object_name='obj'
class IntegranteFInsertar(generic.CreateView):
    model=IntegranteF
    context_object_name="obj"
    template_name="insertar_integrantef.html"
    form_class=IntegranteFForm
    success_url=reverse_lazy('FutsalFem:integrantef_list')
class IntegranteFEditar(generic.UpdateView):
    model=IntegranteF
    context_object_name="obj"
    template_name="insertar_integrantef.html"
    form_class=IntegranteFForm
    success_url=reverse_lazy('FutsalFem:integrantef_list')
class IntegranteFEliminar(generic.DeleteView):
    model = IntegranteF
    template_name="integrantef_borrar.html"
    context_object_name="obj"
    success_url=reverse_lazy("FutsalFem:integrantef_list")