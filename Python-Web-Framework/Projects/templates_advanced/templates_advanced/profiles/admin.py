from django.contrib import admin
from django.contrib.admin import register
from templates_advanced.profiles.models import Profile


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
