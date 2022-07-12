from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("app1中的index方法")


def show(request, id):
    return HttpResponse("app1中的show方法，参数为id，值为" + str(id))
