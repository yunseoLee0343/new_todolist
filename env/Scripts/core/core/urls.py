from django.contrib import admin
from django.urls import path
from todolist.views import todo_list, edit_item, delete_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='todo_list'),
]

