from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserEditForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm

class LoginUserView(LoginView):
    template_name = 'login.html'

class PaginaInicial(TemplateView):
    template_name = "index.html"

class UserListView(ListView):
    model = CustomUser
    template_name = 'listar_usuarios.html'

class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'formulario_usuarios.html'
    success_url = reverse_lazy('login')

class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserEditForm
    template_name = 'formulario_usuarios.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'deletar_usuarios.html'
    success_url = reverse_lazy('user_list')
