from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(generic.TemplateView):
    template_name="home.html"
# Create your views here.
