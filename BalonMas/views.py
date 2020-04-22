from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from BalonMas.models import IntegranteB
from BalonMas.form import IntegranteBForm
from django.http import  HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IntegranteBView(generic.ListView):
    model=IntegranteB
    template_name='integranteb_list.html'
    context_object_name='obj'
class IntegranteBInsertar(generic.CreateView):
    model=IntegranteB
    context_object_name="obj"
    template_name="insertar_integranteb.html"
    form_class=IntegranteBForm
    success_url=reverse_lazy('BalonMas:integranteb_list')
class IntegranteBEditar(generic.UpdateView):
    model=IntegranteB
    context_object_name="obj"
    template_name="insertar_integranteb.html"
    form_class=IntegranteBForm
    success_url=reverse_lazy('BalonMas:integranteb_list')
class IntegranteBEliminar(generic.DeleteView):
    model = IntegranteB
    template_name="integranteb_borrar.html"
    context_object_name="obj"
    success_url=reverse_lazy("BalonMas:integranteb_list")