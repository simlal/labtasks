from django.shortcuts import render
from contact_email.models import Contact
from contact_email.forms import ContactForm

labs = [
    {"id":1, "name":"First Lab"},
    {"id":2, "name":"Second Lab"},
    {"id":3, "name":"Third Lab"},
]

def index(request):
    # Contact form validation
    form = ContactForm(request.POST)
    context = {
        "form" : form,
        "submitted": False,
    }
    print(context)
    return render(request, "base/index.html", context)

def spaces(request, pk):
    return render(request, "base/spaces.html")

def register(request):
    return render(request, "base/register.html")

def login(request):
    return render(request, "base/login.html")
