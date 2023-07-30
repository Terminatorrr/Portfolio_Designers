from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Administration import views

urlpatterns = [
    re_path(r'^delete_portf/(?P<item_id>\w+)/$', views.delete_portf, name='delete_portf'),
    re_path(r'^delete_order/(?P<item_id>\w+)/$', views.delete_order, name='delete_order'),
    re_path(r'^confirm_order/(?P<item_id>\w+)/$', views.confirm_order, name='confirm_order'),
    re_path(r'^administration/', views.administr, name='Administration'),
]
