#from django.contrib import admin
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from homeapp.views import Home
urlpatterns= [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='homeapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homeapp/login.html'), name='logout'),
]