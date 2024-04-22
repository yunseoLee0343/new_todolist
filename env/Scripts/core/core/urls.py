from django.urls import path
from django.contrib import admin
from todolist.views import todo_list, edit_item, delete_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='todo_list'),
    path('edit/<int:pk>/', edit_item, name='edit_item'),
    path('delete/<int:pk>/', delete_item, name='delete_item'),
]
