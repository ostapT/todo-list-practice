from django.urls import path

from todo_list.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView, TagDeleteView, \
    TagCreateView, TagUpdateView, TagListView, set_task_status

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("/create", TaskCreateView.as_view(), name="task-create"),
    path("/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
    path("/<int:pk>/set-task-status/", set_task_status, name="set-task-status")

]

app_name = "todo_list"
