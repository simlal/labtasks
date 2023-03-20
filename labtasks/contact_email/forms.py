from django.forms import ModelForm
from django import forms

from .models import Contact

class ContactForm(ModelForm):
    first_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder" : "First Name"}),
    )
    last_name = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder" : "Last Name"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder" : "Your email"})
    )
    subject = forms.CharField(
        required=True,
        
    )
    message = forms.CharField(
        required=True,
        min_length=50,
        max_length=2000,
        widget= forms.Textarea(attrs={"placeholder" : "Write your message"}),
    )
   


    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "email", "subject", "message"]
        