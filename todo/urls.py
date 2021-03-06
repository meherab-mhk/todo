from django.urls import path

from .views import (
    todo_list, 
    todo_detail, 
    todo_create, 
    todo_update,
    todo_delete,
    
)
app_name = 'todos'

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/',todo_create),
    path('<id>/', todo_detail),
    path('<id>/update/', todo_update, name='todo_update'),
    path('<id>/delete/', todo_delete,)
]