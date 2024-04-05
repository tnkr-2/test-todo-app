from django.db import models
from UserApp.models import CustomUser

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_detail = models.TextField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )

    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
