from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Price import views

urlpatterns = [
    re_path(r'^order_adding/$', views.order_adding, name='order_adding'),
    re_path(r'^delete_adding/(?P<item_id>\w+)/$', views.delete_adding, name='delete_adding'),
    re_path(r'^basket_adding/(?P<item_id>\w+)/$', views.basket_adding, name='basket_adding'),
    re_path(r'^price/', views.price, name='Price'),
]
