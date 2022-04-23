from django.contrib import admin
from django.contrib.admin import register
from templates_advanced.pythons_auth.models import PythonsUser


@register(PythonsUser)
class PythonsUserAdmin(admin.ModelAdmin):
    pass
