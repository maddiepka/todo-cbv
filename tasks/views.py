from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'tasks/tasks.html'

    context_object_name = 'tasks'
    
class TaskDetail(DetailView):
    model = Task
    template_name='tasks/task.html'

    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'

    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')