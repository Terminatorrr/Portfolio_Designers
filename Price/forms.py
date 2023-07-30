from django import forms
from .models import *


class PriceForm(forms.Form):
    nmb = forms.IntegerField(required=True)





class OrderForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    adress = forms.CharField(required=True)
    coments = forms.CharField(required=True)
