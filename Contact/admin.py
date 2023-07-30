from django.contrib import admin
from .models import *


class AskAdmin(admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for field in Ask._meta.fields]
    class Meta:
        model = Ask

admin.site.register(Ask, AskAdmin)
