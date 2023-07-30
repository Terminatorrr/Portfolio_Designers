from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User




class Product(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    image = models.ImageField(upload_to=('product_images/'), blank=True, null=True, default=None)
    describe = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)



# class Temperary(models.Model):
#     product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all prodducts in orders
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=13, blank=True, null=True, default=None)
    customer_adress = models.CharField(max_length=128, blank=True, null=True, default=None)
    coments = models.TextField(blank=True, null=True, default=None)
    status = models.BooleanField(blank=True, null=True, default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  "Order %s %s" % (self.id, self.customer_name)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):


        super(Order,self).save(*args, **kwargs)

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE )
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  "%s" % self.product.name

    class Meta:
        verbose_name = 'Product in order'
        verbose_name_plural = 'Productes in order'



def product_in_order_post_save(sender,  instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.price_per_item
    instance.order.price_per_item = order_total_price
    instance.order.save(force_update=True)
post_save.connect(product_in_order_post_save, sender = ProductInOrder)



class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  "%s" % self.product.name

    class Meta:
        verbose_name = 'Product in basket'
        verbose_name_plural = 'Productes in basket'



