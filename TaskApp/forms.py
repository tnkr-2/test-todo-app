from django import forms
from .models import Task, Priority, Category
from datetime import datetime


class TaskCreateForm(forms.ModelForm):
    task_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', },
    ))
    task_detail = forms.CharField(widget=forms.Textarea(
        attrs={"rows": "4", 'class': 'form-control', },
    ))
    due_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'},
    ))
    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
        )

    class Meta:
        model = Task
        fields = ('task_name', 'task_detail', "priority", "category", 'due_date')

    def save(self):
        task = super(TaskCreateForm, self).save(commit=False)
        task.user = self.user
        task.save()
        return task


class TaskUpdateForm(forms.ModelForm):
    task_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', },
    ))
    task_detail = forms.CharField(widget=forms.Textarea(
        attrs={"rows": "4", 'class': 'form-control', },
    ))
    due_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'},
    ))

    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
        )

    class Meta:
        model = Task
        fields = ('task_name', 'task_detail', 'due_date', 'is_completed', "priority", "category")

    def save(self):
        task = super(TaskUpdateForm, self).save(commit=False)
        if task.is_completed is True:
            task.completed_at = datetime.now()
        task.updated_at = datetime.now()
        task.save()
        return task