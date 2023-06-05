from django.urls import path
from . import views

urlpatterns = [
        path('', views.ApiUrl, name='api-url'),
        path('todo-list/', views.TodoList, name='todo-list'), 
        path('todo-body/<str:pk>/', views.TodoBody, name='todo-body'),
        path('todo-update/<str:pk>/', views.TodoUpdate, name='todo-update'),
        path('todo-create/', views.TodoCreate, name='todo-create'),
        path('todo-delete/<str:pk>', views.TodoDelete, name='todo-delete')
        ]


