from django.contrib import admin
from django.contrib.admin import register
from petstagram.common.models import Comment


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
