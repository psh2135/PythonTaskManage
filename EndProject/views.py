from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Task, Team
from .forms import CustomUserCreationForm,CustomAuthenticationForm, TaskForm, ChooseTeamForm
from django.db import transaction
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

#home
def home(request):
    return render(request, "home.html")

# REGISTER
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("choose_team")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


# LOGIN
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "login.html", {"form": form})


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect("home")

#user
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'Users/User_list.html', {'Users': users})

from django.shortcuts import render, redirect

@login_required
def choose_team(request):
    if request.method == "POST":
        form = ChooseTeamForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            role = form.cleaned_data['role']
            user = request.user
            user.role = role
            user.myTeam = team  # בהתאם לשדה שלך במודל User
            user.save()
            return redirect("home")
    else:
        form = ChooseTeamForm()
    return render(request, "Users/choose_team.html", {"form": form})

#tasks
@login_required
def task_list(request):
    user = request.user
    tasks = Task.objects.filter(myTeam=user.myTeam)
    return render(request, 'Tasks/task_list.html', {'Tasks': tasks})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.role == "admin" and task.myDoner is None :
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_list')
        else:
            form = TaskForm(instance=task)
        return render(request, 'Tasks/task_form.html', {'form': form})
    else:
        return redirect('task_list')
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.role == "admin" and task.myDoner is None:
        if request.method == "POST":
            task.delete()
            return redirect('task_list')
        return render(request, 'Tasks/task_confirm_delete.html', {'task': task})
    else:
        return redirect('task_list')
@login_required
@transaction.atomic
def task_create(request):
    if request.user.role == "admin":
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('task_list')
        else:
            form = TaskForm()
    else:
        return redirect('task_list')
    return render(request, 'Tasks/task_form.html', {'form': form})

@login_required
def task_take(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.myDoner is None and request.user.role == "worker":
        task.myDoner = request.user
        task.status = "process"
        task.save()
    return redirect('task_list')
