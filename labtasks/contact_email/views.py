from django.shortcuts import render

def header_error(request):
    return render(request, "contact_email/header_error.html")