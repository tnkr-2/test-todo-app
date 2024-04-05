from django import forms
from .models import CustomUser

from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', },
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', },
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', },
    ))
    birthday = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)','class': 'form-control', },
    ))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', },
            ))
    password2 = forms.CharField(
        label="Password (confirm)",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', },
            ))

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "birthday")
