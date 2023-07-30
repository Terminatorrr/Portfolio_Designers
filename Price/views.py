from django.shortcuts import render, redirect
from .models import *
from .forms import *


def basket_adding(request, item_id):
    return_dict = dict()

    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    print(data)
    product_id = item_id
    product = Product.objects.get(id=product_id)
    new_product, created= ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, price_per_item=product.price)
    if not created:
        new_product.save(force_update=True)
    return redirect('/price')


def price(request):
    form = PriceForm(request.POST or None)
    session_key = request.session.session_key
    product = Product.objects.filter()
    order = Order.objects.filter()
    product_in_order = ProductInOrder.objects.filter()
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)


    if request.method == 'POST':

        data = request.POST
        print(request.POST)
        product_id = data.get("id")
        product_id1 = data.get("product_id")
        print(product_id, product_id1)
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id)
    return render(request, 'Price/Price.html', locals())



def delete_adding(request, item_id):
    ProductInBasket.objects.filter(id=item_id).delete()
    return redirect('/price')

def order_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key).exclude(order__isnull=False)
    form = OrderForm(request.POST or None)
    if request.method == "POST":
        print(request.POST)

        print("Yes")
        data = request.POST
        name = data.get("name", "Unknowing")
        adress = data['adress']
        coments = data['coments']
        phone = data['phone']
        order = Order.objects.create(customer_name=name, customer_phone=phone, customer_adress=adress, coments=coments)

        for name, value in data.items():
            print(name.split("product_in_basket_"))
            if name.startswith("product_in_basket_"):
                print(name.split("product_in_basket_")[1])
                product_in_basket_id = name.split("product_in_basket_")[1]
                product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)
                product_in_basket.nmb = value
                product_in_basket.save(force_update = True )

                ProductInOrder.objects.create(product=product_in_basket.product, price_per_item=product_in_basket.price_per_item, order=order)
                ProductInBasket.objects.all().delete()
        else:
            print("No")

    return render(request, 'Price/Order.html', locals())
