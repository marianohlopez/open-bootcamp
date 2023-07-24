from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm


def form(request):
    comment_form = CommentForm(
        {"name": "Mariano", "url": "https://open-bootcamp.com", "comment": "Comentario"})
    return render(request, "form.html", {"comment_form": comment_form})


def goal(request):
    if request.method != "POST":
        return HttpResponse("metodo no permitido")

    return HttpResponse(request.POST["name"])
