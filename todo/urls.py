from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
    path('todo/', views.TodoList.as_view()),
    path('todo/<int:pk>/', views.TodoDetail.as_view()),
]