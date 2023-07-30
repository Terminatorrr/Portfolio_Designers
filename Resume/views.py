from django.shortcuts import render
# from products.models import *


def resume(request):
    # products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    # products_images_phones = products_images.filter(product__category__id=1)
    # products_images_pc = products_images.filter(product__category__id=3)
    return render(request, 'Resume/Resume.html', locals())
