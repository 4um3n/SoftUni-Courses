from django.shortcuts import render, redirect
from todo.todo_app.models import Todo
from todo.todo_app.forms import TodoForm

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo_app/index.html', context)


def save_todo(request):
    title = request.POST['title']
    description = request.POST['description']

    todo = Todo(
        title=title,
        description=description,
    )
    todo.is_done = False
    todo.save()
    return redirect('/')


def create(request):
    context = None
    form = TodoForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            todo = Todo(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
            )
            todo.save()
            return redirect("index")

        context = {"form": form}

    context = {"form": TodoForm()} if context is None else context
    return render(request, 'todo_app/create.html', context)


def update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    form = TodoForm(request.POST, initial=todo.__dict__)
    if request.method == "POST":
        if form.is_valid():
            todo.title = form.cleaned_data["title"]
            todo.description = form.cleaned_data["description"]
            todo.save()
            return redirect("index")

    context = {
        "form": form,
        "todo": todo,
    }
    return render(request, 'todo_app/edit.html', context)


def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect("index")




