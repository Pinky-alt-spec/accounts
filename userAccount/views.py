from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    conditions = Condition.objects.all()
    users = User.objects.all()

    total_users = users.count()

    total_conditions = conditions.count()
    current = conditions.filter(status='Current').count()
    completed = conditions.filter(status='Completed').count()
    deleted = conditions.filter(status='Deleted').count()

    context = {
        'conditions': conditions,
        'users': users,
        'total_conditions': total_conditions,
        'current': current,
        'completed': completed,
        'deleted': deleted,
    }
    return render(request, 'userAccount/dashboard.html', context)


def task(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'userAccount/tasks.html', context)


def user(request):
    return render(request, 'userAccount/user.html')
