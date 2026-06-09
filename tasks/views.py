
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task, UserProfile
from django.contrib.auth.models import User
from .forms import TaskForm


@login_required(login_url='login')
def task_list(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('update_profile')

    tasks = Task.objects.filter(team_name=profile.team_name)
    user_filter = request.GET.get('user')
    is_filtered = False

    if user_filter:
        tasks = tasks.filter(assigned_to__id=user_filter)
        is_filtered = True

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'profile': profile,
        'team_name': profile.team_name,
        'is_filtered': is_filtered
    })


@login_required
def add_task(request):
    profile = request.user.profile
    if profile.role != 'manager':
        return redirect('task_list')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.team_name = profile.team_name
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form, 'edit_mode': False})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, team_name=request.user.profile.team_name)#האם המשתמש שגולש קיים בצוות של המשימה הזו והאם קיימת משימה כזו
    profile = request.user.profile

    if profile.role != 'manager' or task.assigned_to is not None:#תכנס רק אם אתה מנהל ורק אם אף אחד לא שייך אליו את המשימה הזו
        return redirect('task_list')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/add_task.html', {'form': form, 'edit_mode': True})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, team_name=request.user.profile.team_name)# והאם המשימה הספציפית שייכת למשתמש שגולש כרגע האם קיימת משימה כזו
    if request.user.profile.role == 'manager' and not task.assigned_to:#השדה משויך ל -  הוא ריק ?בדיקה האם אתה מנהל והאם
        task.delete()#מחיקה מהדאטה בייס
    return redirect('task_list')#חזרה למשימות


@login_required
def claim_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, team_name=request.user.profile.team_name)
    if not task.assigned_to:
        task.assigned_to = request.user
        task.status = 'in_progress'
        task.save()
    return redirect('task_list')


@login_required
def update_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id, team_name=request.user.profile.team_name)

        if task.status == 'completed':
            return redirect('task_list')

        new_status = request.POST.get('status')
        if task.assigned_to == request.user or request.user.profile.role == 'manager':
            task.status = new_status
            task.save()
    return redirect('task_list')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('update_profile')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})


@login_required
def update_profile(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        role = request.POST.get('role')
        UserProfile.objects.update_or_create(
            user=request.user,
            defaults={'team_name': team_name, 'role': role}
        )
        return redirect('task_list')
    existing_teams = UserProfile.objects.values_list('team_name', flat=True).distinct()
    return render(request, 'tasks/profile.html', {'existing_teams': existing_teams})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
