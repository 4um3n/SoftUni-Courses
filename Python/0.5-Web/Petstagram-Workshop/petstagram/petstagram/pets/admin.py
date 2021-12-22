from django.contrib import admin
from petstagram.pets.models import Pet, Like

# Register your models here.


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'age', 'likes_count')
    list_filter = ('name', )

    def likes_count(self, obj):
        return obj.likes_count


admin.site.register(Pet)
admin.site.register(Like)
