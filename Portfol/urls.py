from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from Portfol import views

urlpatterns = [

    re_path(r'^portfolio/', views.portfolio, name='Portfolio'),
]
