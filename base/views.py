from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Deposit
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    

class Home(LoginRequiredMixin, ListView):
    model = Deposit
    context_object_name = 'deposits'
    template_name = 'base/deposit_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deposits'] = context['deposits'].filter(user=self.request.user)
        context['count'] = context['deposits'].filter(user=self.request.user).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['deposits'] = context['deposits'].filter(
                title__startswith=search_input)
            
        context['search_input'] = search_input
        
        return context


class DepositDetail(DetailView):
    model = Deposit
    context_object_name = 'deposit'
    template_name = 'base/deposit_detail.html'


class DepositCreate(CreateView):
    model = Deposit
    fields = ['title', 'email', 'pix', 'amount', 'description']
    success_url = reverse_lazy('home')
    template_name = 'base/deposit_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DepositCreate, self).form_valid(form)


class DepositUpdate(UpdateView):
    model = Deposit
    fields = ['title', 'email', 'pix', 'amount', 'description']
    success_url = reverse_lazy('home')
    template_name = 'base/deposit_form.html'


class DepositDelete(DeleteView):
    model = Deposit
    success_url = reverse_lazy('home')
    context_object_name = 'deposit'
    template_name = 'base/deposit_confirm_delete.html'
