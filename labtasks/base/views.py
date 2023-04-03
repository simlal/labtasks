from django.shortcuts import render
from django.utils import timezone

from contact_email.models import Contact
from contact_email.forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings



def returned_message(first_name):
    message = f"""
        Hello {first_name},
        Thank you for contacting us at 🧪 LaboraTasks 🥼. Our team will get back to you ASAP.

        In the meantime, stay safe!
        𝙏𝙝𝙚 𝙇𝙖𝙗𝙤𝙧𝙖𝙏𝙖𝙨𝙠𝙨 𝙏𝙚𝙖𝙢
        """
    return message

def index(request):
    submitted=False
    # Form validation and saving to db with the associated model
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            cd = contact.cleaned_data
            if cd["last_name"] == "":    # Changing not-required field to NULL val
                cd["last_name"] = None
            # Adding submit date (save to db) but not in form
            contact_instance = contact.save(commit=False)
            contact_instance.send_date = timezone.now()
            contact_instance.save()
            submitted = True
            context = {
                "form" : contact,
                "submitted" : submitted
            }
            # Sending confirmation email
            form_vals = "\n".join(cd.values())
            try:
                send_mail(
                    subject=f"LaboraTasks confirmation: '{cd['subject']}'",
                    message=returned_message(cd["first_name"]),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[cd["email"]]
                )
                print(form_vals)
                print(returned_message(cd["first_name"]))
            except BadHeaderError:
                return render(request, "contact_email/header_error.html")

            return render(request, "base/index.html", context=context)
    
    # To render contact form
    else :
        contact = ContactForm()
        submitted = False

    context = {
        "form" : contact,
        "submitted": submitted,
    }
    # print(context)
    return render(request, "base/index.html", context=context)
