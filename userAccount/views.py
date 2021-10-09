from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'userAccount/dashboard.html')


def tasks(request):
    return render(request, 'userAccount/tasks.html')


def user(request):
    return render(request, 'userAccount/user.html')