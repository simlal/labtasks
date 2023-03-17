from django.shortcuts import render

labs = [
    {"id":1, "name":"First Lab"},
    {"id":2, "name":"Second Lab"},
    {"id":3, "name":"Third Lab"},
]

def index(request):
    context = {"labs" : labs}
    return render(request, "base/index.html", context)

def spaces(request, pk):
    return render(request, "base/spaces.html")

def register(request):
    return render(request, "base/register.html")

def login(request):
    return render(request, "base/login.html")
