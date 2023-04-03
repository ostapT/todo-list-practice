from django.urls import path

from todo_list.views import TaskList

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
]

app_name = "todo_list"
