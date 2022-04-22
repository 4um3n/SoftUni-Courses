from django.contrib import admin
from expenses_tracker.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
