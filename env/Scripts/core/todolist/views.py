from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    todo_items = TodoItem.objects.all()
    form = TodoItemForm()
    return render(request, 'todolist/todo_list.html', {'todo_items': todo_items, 'form': form})

def edit_item(request, pk):
    item = TodoItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=item)
    return render(request, 'todolist/edit_item.html', {'form': form})

def delete_item(request, pk):
    item = TodoItem.objects.get(pk=pk)
    item.delete()
    return redirect('todo_list')
