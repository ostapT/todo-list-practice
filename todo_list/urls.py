from django.urls import path

from todo_list.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("/create", TaskCreateView.as_view(), name="task-create"),
    path("/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

]

app_name = "todo_list"
