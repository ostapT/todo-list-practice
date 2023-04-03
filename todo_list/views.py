from django.shortcuts import render
from django.views import generic

from todo_list.models import Task


class TaskList(generic.ListView):
    model = Task
