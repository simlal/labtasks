from django.forms import ModelForm
from django import forms

from .models import Labspace, Message

class LabspaceForm(ModelForm):
    name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder" : "Labspace name"}),
    )
    
    description = forms.CharField(
        required=True,
        max_length=200,
        widget= forms.Textarea(attrs={"placeholder" : "Write a description for the labspace"}),
    )
    
    class Meta:
        model = Labspace
        fields = ["name", "description"]

class editLabspaceForm(ModelForm):
    name = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder" : "Enter new Labspace name"}),
    )
    
    description = forms.CharField(
        required=False,
        max_length=200,
        widget= forms.Textarea(attrs={"placeholder" : "Enter new description"}),
    )
    
    class Meta:
        model = Labspace
        fields = ["name", "description"]

class PostMessageForm(ModelForm):
    body = forms.CharField(
        required=True,
        max_length=2000,
        widget=forms.Textarea(attrs={"placeholder": "Write your message here."})
    )
    
    class Meta:
        model = Message
        fields = ["body"]