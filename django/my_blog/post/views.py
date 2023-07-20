from django.shortcuts import render
from .models import Author
from django.http import HttpResponse


def update(request):
    author = Author.objects.get(id=1)
    author.name = "Juanjo"
    author.email = "juango@demo.com"
    author.save()
    return HttpResponse("modificado")
