from django.contrib import admin
from django.contrib.admin import register
from notes.common.models import Profile, Note


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
