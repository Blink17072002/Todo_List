from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('', views.Todo, name='Todo'),
    path('completed/', views.completed, name='completed'),
    path('not_completed/', views.not_completed, name='not_completed'),
    path('completed/<int:todo_item_id>/', views.completed_todo_item, name='completed'),
]
