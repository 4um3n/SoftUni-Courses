from django.contrib import admin
from django.contrib.admin import register

from petstagram.accounts.models import UserProfile


@register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

