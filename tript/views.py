from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import (TemplateView, DetailView, FormView, ListView, CreateView, DeleteView, UpdateView)
from tript.forms import UserCreateForm#,TriptUserForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LandingView(TemplateView):
  template_name='landing.html'

class LoginUserView(LoginView):
  template_name='login.html'

class SignUpView(CreateView):
  context_object_name= 'user_create'
  form_class = UserCreateForm
  success_url = reverse_lazy('login')
  template_name='signup.html'

class DashboardView(LoginRequiredMixin,TemplateView):
  template_name='dashboard.html'


