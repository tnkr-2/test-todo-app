from django.urls import path
from .views import (
    TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView, HomeView
    )

app_name = "taskapp"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("home/", HomeView.as_view(), name="home"),
    path("task_create/", TaskCreateView.as_view(), name="task_create"),
    path("task_list/", TaskListView.as_view(), name="task_list"),
    path("task_detail/<int:pk>", TaskDetailView.as_view(), name="task_detail"),
    path("task_update/<int:pk>", TaskUpdateView.as_view(), name="task_update"),
    path("task_delete/<int:pk>", TaskDeleteView.as_view(), name="task_delete"),
]
