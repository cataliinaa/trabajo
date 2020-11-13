from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm;
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/Registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('homeUsuario')
 
 
class UserList(ListView):
    model = User
    template_name = 'Usuario/List_user.html'
