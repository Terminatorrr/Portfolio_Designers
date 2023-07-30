from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Service import views

urlpatterns = [

    re_path(r'^service/', views.service, name='Service'),
]
