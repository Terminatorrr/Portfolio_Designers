from django.shortcuts import render, redirect
from Portfol.models import *
from Contact.models import *
from Price.models import *
from .forms import AddForm
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def administr(request):




    Ask_masage = Ask.objects.filter()
    portfolio_images = Portfolio.objects.filter()
    orders = ProductInOrder.objects.filter()
    session_key = request.session.session_key
    form = AddForm(request.POST, request.FILES)
    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            form.save()


        else:
            form = AddForm()
            print("No")



    return render(request, 'Administration/Administration.html', locals())


def delete_portf(request, item_id):
    Portfolio.objects.filter(id=item_id).delete()
    return redirect('/administration')

def delete_order(request, item_id):
    ProductInOrder.objects.filter(id=item_id).delete()
    return redirect('/administration')

def confirm_order(request, item_id):
    prod = ProductInOrder.objects.get(id=item_id)
    order_id=prod.order.id
    print(order_id)
    order=Order.objects.get(id=order_id)
    order.status=True
    order.save()

    return redirect('/administration')
