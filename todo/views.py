from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import TodoForm
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context = {
        "todo_list": todos
    }
    return render(request,"todo/todo_list.html", context)

#CRUD , Create , retrieve , update , delete , delete

def todo_detail(request, id=None):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return None
    context = {
        "todo": todo
    }
    return render(request,"todo/todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # name        = form.cleaned_data['name']
        # due_date    = form.cleaned_data['due_date']
        # print(name,due_date)

        # new_todo = Todo.objects.create(name=name,due_date=due_date)
        # pass
        form.save()
        return redirect('/')
    context = {
        "form": form
    }
    return render(request, "todo/todo_create.html",context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        "form": form
    }
    return render(request, "todo/todo_update.html",context)
    
def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')