from django.shortcuts import render
from django.utils import timezone

from contact_email.models import Contact
from contact_email.forms import ContactForm



def returned_message(first_name):
    message = f"""
        Hello {first_name},
        Thank you for contacting us at 🧪 LaboraTasks 🥼. Our team will get back to you ASAP.

        In the meantime, stay safe!
        \x1B[1;3mThe LaboraTask team\x1B[0;3m
        """

def index(request):
    
    submitted=False
    # Form validation and saving to db with the associated model
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            cd = contact.cleaned_data
            if cd["last_name"] == "":    # Changing not-required field to NULL val
                cd["last_name"] = None
            contact_instance = contact.save(commit=False)   # To add the submit date but not using the form fields
            contact_instance.send_date = timezone.now()
            contact_instance.save()
            submitted = True
    
    # To render contact form
    else :
        contact = ContactForm()
        submitted = False

    context = {
        "form" : contact,
        "submitted": submitted,
    }
    # print(context)
    return render(request, "base/index.html", context)

def spaces(request, pk):
    return render(request, "base/spaces.html")

def register(request):
    return render(request, "base/register.html")

def login(request):
    return render(request, "base/login.html")
