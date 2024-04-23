# todolist/views.py

from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    # 세션에서 Todo 아이템 목록을 가져옵니다. 없으면 빈 리스트를 반환합니다.
    todo_items = request.session.get('todo_items', [])

    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            # 새로운 Todo 아이템을 추가하고 세션을 업데이트합니다.
            todo_items.append(form.cleaned_data['item_text'])
            request.session['todo_items'] = todo_items
            return redirect('todo_list')
    else:
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
