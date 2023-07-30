from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

# class TemperaryInline(admin.TabularInline):
#     model = ProductInOrder
#     extra = 0
#
# class TemperaryAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Product._meta.fields]
#     inlines = [Temperary]
#     class Meta:
#         model = Temperary
#
# admin.site.register(Temperary, TemperaryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)
