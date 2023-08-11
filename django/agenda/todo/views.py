from django.shortcuts import render
from .models import Todo


def index(request):
    todos = Todo.objects.filter(title__contains=request.GET.get("search", ""))
    context = {
        "todos": todos
    }
    return render(request, "todo/index.html", context)


def view(request, id):
    return render(request, "todo/index.html", {})


def edit(request, id):
    return render(request, "todo/index.html", {})


def delete(request, id):
    return render(request, "todo/index.html", {})


def create(request, id):
    return render(request, "todo/index.html", {})
