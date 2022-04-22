from django.contrib import admin
from django.contrib.admin import register

from recipes.common.models import Recipe


@register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
