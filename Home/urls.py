from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Home import views

urlpatterns = [

    re_path(r'^$', views.home, name='About_us'),
]
