from django.urls import path
from .views import index, todos, login, register

urlpatterns = [
    path('', index, name='index'),
    path('todos/', todos, name='todos'),
    path('accounts/login', login, name='login'),
    path('accounts/register', register, name='register')
]