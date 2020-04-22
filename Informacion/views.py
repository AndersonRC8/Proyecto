from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.
class InformacionDeportes(generic.TemplateView):
    template_name="informacion_deportes.html"
