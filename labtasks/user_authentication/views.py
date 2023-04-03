from django.shortcuts import render

def register(request):
    return render(request, "user_authentication/register.html")

def login(request):
    return render(request, "user_authentication/login.html")
