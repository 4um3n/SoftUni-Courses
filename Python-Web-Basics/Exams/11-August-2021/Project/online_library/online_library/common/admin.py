from django.contrib import admin
from django.contrib.admin import register
from online_library.common.models import Profile, Book


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
