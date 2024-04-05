from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


# Create your views here.


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'userapp/signup.html'
    success_url = reverse_lazy("userapp:login")


class LoginView(LoginView):
    template_name = 'userapp/login.html'
    success_url = reverse_lazy("taskapp:task_list")


class LogoutView(LogoutView):
    pass
