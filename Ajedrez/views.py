from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from Ajedrez.models import IntegranteA
from Ajedrez.form import IntegranteAForm
from django.http import  HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IntegranteAView(generic.ListView):
    model=IntegranteA
    template_name='integrantea_list.html'
    context_object_name='obj'
class IntegranteAInsertar(generic.CreateView):
    model=IntegranteA
    context_object_name="obj"
    template_name="insertar_integrantea.html"
    form_class=IntegranteAForm
    success_url=reverse_lazy('Ajedrez:integrantea_list')
class IntegranteAEditar(generic.UpdateView):
    model=IntegranteA
    context_object_name="obj"
    template_name="insertar_integrantea.html"
    form_class=IntegranteAForm
    success_url=reverse_lazy('Ajedrez:integrantea_list')
class IntegranteAEliminar(generic.DeleteView):
    model = IntegranteA
    template_name="integrantea_borrar.html"
    context_object_name="obj"
    success_url=reverse_lazy("Ajedrez:integrantea_list")