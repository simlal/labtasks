from django.forms import ModelForm
from django import forms

from .models import Contact

class ContactForm(ModelForm):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=False, max_length=50)
    message = forms.CharField(
        widget= forms.Textarea(
            attrs= {
                "placeholder" : "Write your message",
            },
        ),
        max_length=2000
    )

    class Meta:
        model = Contact
        fields = '__all__'
