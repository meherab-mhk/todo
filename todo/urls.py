from django.urls import path

from .views import todo_list, todo_detail, todo_create, todo_update

app_name = 'todos'

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/',todo_create),
    path('<int:id>/', todo_detail),
    path('update/<int:id>/', todo_update, name='todo_update'),
]