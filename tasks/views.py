from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .forms import UserRegisterForm

# Create your views here.

class LoginPage(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')

class RegisterPage(CreateView):
    template_name = 'tasks/register.html'
    form_class = UserRegisterForm

    success_message='Your profile was created successfully'
    success_url = reverse_lazy('tasks')

    redirect_authenticated_user = True




class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks.html'

    context_object_name = 'tasks'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__contains=search_input)

        return context
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name='tasks/task.html'

    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed']

    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')