from django.contrib import admin
from django.contrib.admin import register
from petstagram.pets.models import Pet, Like, Comment


@register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'type', 'age')
    list_filter = ('type', 'age')
    sortable_by = ("age", "name")
    #
    # @staticmethod
    # def likes_count(obj):
    #     return obj.likes_count

# admin.site.register(Pet, PetAdmin)


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
