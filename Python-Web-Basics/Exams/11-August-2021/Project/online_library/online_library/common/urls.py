from django.urls import path

from online_library.common.views import home_page, add_book, edit_book, book_details, delete_book, \
    profile_page, edit_profile, delete_profile


urlpatterns = [
    path("", home_page, name="home"),
    path("add/", add_book, name="add book"),
    path("edit/<int:book_pk>", edit_book, name="edit book"),
    path("book/delete/<int:book_pk>", delete_book, name="delete book"),
    path("details/<int:book_pk>", book_details, name="book details"),
    path("profile/", profile_page, name="profile"),
    path("profile/edit/", edit_profile, name="edit profile"),
    path("profile/delete/", delete_profile, name="delete profile"),
]
