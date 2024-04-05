from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import TaskCreateForm, TaskUpdateForm
from .models import Task


# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'taskapp/task_create.html'
    success_url = reverse_lazy("taskapp:task_list")

    def form_valid(self, form):
        form.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("taskapp:task_list")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'taskapp/task_list.html'

    def get_queryset(self):
        query = super().get_queryset()
        user_id = self.request.user.id
        query = Task.objects.filter(user_id=user_id)
        date_sort = self.request.GET.get("date_sort", None)
        category = self.request.GET.get("category", None)
        completed = self.request.GET.get("completed", None)

        if date_sort == "1":
            query = query.order_by("due_date")
        if date_sort == "2":
            query = query.order_by("-due_date")

        if date_sort == "3":
            query = query.order_by("updated_at")
        if date_sort == "4":
            query = query.order_by("-updated_at")

        if category == "1":
            query = query.filter(category_id="1")
        if category == "2":
            query = query.filter(category_id="2")

        if completed:
            if completed == "1":
                query = query.filter(is_completed=True)
            if completed == "2":
                query = query.filter(is_completed=False)
        else:
            query = query.filter(is_completed=False)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_sort = self.request.GET.get("date_sort", None)
        category = self.request.GET.get("category", None)
        completed = self.request.GET.get("completed", None)
        context["completed"] = "2"

        if completed:
            context["completed"] = completed
        if date_sort:
            context["date_sort"] = date_sort
        if category:
            context["category"] = category

        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'taskapp/task_detail.html'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'taskapp/task_update.html'

    def get_success_url(self):
        return reverse_lazy("taskapp:task_detail", kwargs={"pk": self.object.id})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'taskapp/task_delete.html'
    success_url = reverse_lazy("taskapp:task_list")


class HomeView(TemplateView):
    template_name = 'taskapp/home.html'
