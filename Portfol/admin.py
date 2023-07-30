from django.contrib import admin
from .models import *


class PortfolioAdmin(admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for field in Portfolio._meta.fields]
    class Meta:
        model = Portfolio

admin.site.register(Portfolio, PortfolioAdmin)
