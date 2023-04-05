from django.forms import ModelForm
from django import forms

from .models import Labspace

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