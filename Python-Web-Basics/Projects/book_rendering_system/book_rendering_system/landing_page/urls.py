from django.urls import path
from book_rendering_system.landing_page.views import index, create_book, edit_book

urlpatterns = [
    path('', index, name="index"),
    path('create/', create_book, name="create"),
    path('edit/<int:book_id>', edit_book, name="edit"),
]
