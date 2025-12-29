from django import forms
from .models import User, Team, Task


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

    # def clean_username(self):
    #         cUsername = self.cleaned_data["username"]
    #         if not cUsername.is():
    #             raise forms.ValidationError("Should be valid email address")
    #         return cUsername

    # def clean_password(self):
    #         lname = self.cleaned_data["l_name"]
    #         if not lname.isalpha():
    #             raise forms.ValidationError("Should contains only letters")
    #         return lname

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = __all__
        labels = {
            "title": "Title",
            "describe": "Description",
            "deadline":"Deadline",
            "status":"Status",
            "myTeam" : "Team",
            "myDoner": "Doner"
        }

    # def __init__(self, *args, **kwargs):
    #      super().__init__(*args, **kwargs)
    #    #  self.fields["kita"].queryset = Kita.objects.filter(can_register=True)

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["name"]