from django.shortcuts import render
from .models import *


def portfolio(request):
    portfolio_images = Portfolio.objects.filter()

    return render(request, 'Portfolio/Portfolio.html', locals())
