from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from BalonFem.models import IntegranteBF
from BalonFem.form import IntegranteBFForm
from django.http import  HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IntegranteBFView(generic.ListView):
    model=IntegranteBF
    template_name='integrantebf_list.html'
    context_object_name='obj'
class IntegranteBFInsertar(generic.CreateView):
    model=IntegranteBF
    context_object_name="obj"
    template_name="insertar_integrantebf.html"
    form_class=IntegranteBFForm
    success_url=reverse_lazy('BalonFem:integrantebf_list')
class IntegranteBFEditar(generic.UpdateView):
    model=IntegranteBF
    context_object_name="obj"
    template_name="insertar_integrantebf.html"
    form_class=IntegranteBFForm
    success_url=reverse_lazy('BalonFem:integrantebf_list')
class IntegranteBFEliminar(generic.DeleteView):
    model = IntegranteBF
    template_name="integrantebf_borrar.html"
    context_object_name="obj"
    success_url=reverse_lazy("BalonFem:integrantebf_list")