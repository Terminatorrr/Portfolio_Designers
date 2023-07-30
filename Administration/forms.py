from django import forms
from Portfol.models import *


class AddForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ("image", "name", "description")

