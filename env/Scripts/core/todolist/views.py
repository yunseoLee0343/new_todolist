from django.shortcuts import render
from models import TodoItem

def todo_list(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todolist/todo_list.html', {'todo_items': todo_items})
