from django import forms
from .models import *


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)
