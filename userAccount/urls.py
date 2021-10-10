from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.task, name='tasks'),
    path('user/', views.user, name='user'),
]