from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    return render(request, 'index.html')


def todos(request):
    todos = Todo.objects.all()
    return render(request, 'todos.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        text = request.POST['todo_text']
        owner = request.user
        new_todo = Todo.objects.create(text=text, owner=owner)
    return redirect('index')


def delete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
