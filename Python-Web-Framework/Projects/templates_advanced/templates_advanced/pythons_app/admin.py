from django.contrib import admin
from django.contrib.admin import register

from .models import Python


@register(Python)
class PythonAdmin(admin.ModelAdmin):
    pass
