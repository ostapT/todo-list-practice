from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from todo_list.views import TaskList

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "todo_list"
