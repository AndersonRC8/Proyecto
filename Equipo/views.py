from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.
class Equipo(generic.TemplateView):
    template_name="equipo.html"
