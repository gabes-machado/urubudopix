from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Deposit
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    

class Home(ListView):
    model = Deposit
    context_object_name = 'deposits'
    template_name = 'base/deposit_list.html'


class DepositDetail(DetailView):
    model = Deposit
    context_object_name = 'deposit'
    template_name = 'base/deposit_detail.html'


class DepositCreate(CreateView):
    model = Deposit
    fields = ['user', 'title', 'email', 'pix', 'amount', 'description']
    success_url = reverse_lazy('home')
    template_name = 'base/deposit_form.html'


class DepositUpdate(UpdateView):
    model = Deposit
    fields = ['user', 'title', 'email', 'pix', 'amount', 'description']
    success_url = reverse_lazy('home')
    template_name = 'base/deposit_form.html'


class DepositDelete(DeleteView):
    model = Deposit
    success_url = reverse_lazy('home')
    context_object_name = 'deposit'
    template_name = 'base/deposit_confirm_delete.html'