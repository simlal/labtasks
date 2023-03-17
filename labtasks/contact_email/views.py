from django.shortcuts import render

def contact(request):
    return render(request, "contact_email/contact.html")
