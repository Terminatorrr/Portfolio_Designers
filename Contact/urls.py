from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Contact import views

urlpatterns = [

    re_path(r'^contact/', views.contact, name='Contact'),
]
