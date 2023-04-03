from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")



