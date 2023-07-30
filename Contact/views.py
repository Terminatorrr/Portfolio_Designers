from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from .forms import ContactForm
from django.contrib.auth.models import User

def contact(request):
    session_key = request.session.session_key
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            print("Yes")
            data = request.POST
            name = data.get("name", "Unknowing")
            email = data['email']
            subject = data['subject']
            message = data['message']
            user, created = User.objects.get_or_create(username=email, defaults={"first_name": name})

            ask = Ask.objects.create(user = user, customer_name = name, customer_email = email, subject = subject, message = message)

        else:
            print("No")
    # products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    # products_images_phones = products_images.filter(product__category__id=1)
    # products_images_pc = products_images.filter(product__category__id=3)
    return render(request, 'Contact/Contact.html', locals())
