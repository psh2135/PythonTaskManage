from django import forms
from .models import User, Team, Task
from datetime import datetime, timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            "username": "Email",
            "password": "Password"
        }
        help_texts = {
            "username": "Should be valid email address",
            "password": "Should contains letters and numbers",
        }


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ),
        initial=(datetime.today() + timedelta(days=30)).date()
    )
    class Meta:
        model = Task
        fields = ["title", "description", "deadline"]
        labels = {
            "title": "Title",
            "describe": "Description",
            "deadline":"Deadline"
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["name"]


class ChooseTeamForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), empty_label="Select a team")
    role = forms.ChoiceField(choices=[('admin', 'Admin'), ('worker', 'Worker')])