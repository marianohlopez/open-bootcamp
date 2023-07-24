from django.shortcuts import render
from django.http import HttpResponse


def getform(request):
    return render(request, "form.html", {})


def getgoal(request):
    if request.method != "GET":
        return HttpResponse("el metodo POST no esta soportado")

    name = request.GET["name"]
    return render(request, "success.html", {"name": name})


def postform(request):
    return render(request, "postform.html", {})


def postgoal(request):
    if request.method != "POST":
        return HttpResponse("EL metodo get no esta soportado para esta ruta")

    info = request.POST["info"]
    return render(request, "postsuccess.html", {"info": info})
