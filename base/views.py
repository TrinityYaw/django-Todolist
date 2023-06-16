from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormView
from .models import Task
from .forms import TaskForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login
# Create your views here.


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'List'
    template_name = "base/index.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['List'] = context['List'].filter(user = self.request.user)
        

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['List'] = context['List'].filter(title__contains=search_input)
       
        return context  
          
        context['search_input'] = search_input
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'List'
    template_name = "base/detail.html"

 
class CreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView,self).form_valid(form)
    
    

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "base/update.html"
   
    success_url = reverse_lazy('index')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('index')
    context_object_name = 'List'
    template_name = "base/delete.html"


class TaskLogin(LoginView):
    template_name = 'base/login.html'
    fields = ['title', 'description', 'complete']
    redirect_authenticated_user = True
    
    def get_success_url(self):
        
        return reverse_lazy('index')
    


class TaskLogout(LogoutView):
    fields = '__all__'
    next_page = reverse_lazy('login')
    

class RegisterTask(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterTask,self).form_valid(form)
    
    def get_success_url(self):
        
        return reverse_lazy('index')
    