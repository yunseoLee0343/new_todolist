from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.middleware.csrf import get_token
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # 아이템 추가 후 리다이렉트
    else:
        form = TodoItemForm()

    todo_items = TodoItem.objects.all()
    csrf_token = get_token(request)  # CSRF 토큰을 가져옵니다.
    return render(request, 'todolist/todo_list.html', {'todo_items': todo_items, 'form': form, 'csrf_token': csrf_token})

@require_POST
def edit_item(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)
    form = TodoItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True})  # 성공적인 응답을 반환합니다.
    else:
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)  # 실패한 경우 오류와 함께 응답합니다.

@require_POST
def delete_item(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)
    item.delete()
    return JsonResponse({'success': True})  # 성공적인 응답을 반환합니다.
