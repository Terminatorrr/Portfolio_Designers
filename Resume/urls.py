from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Resume import views

urlpatterns = [

    re_path(r'^resume/', views.resume, name='Resume'),
]
