from django.urls import path
from notes.common.views import home, add_note, edit_note, delete_note, note_details, profile, delete_profile

urlpatterns = [
    path("", home, name="home"),
    path("add/", add_note, name="add note"),
    path("edit/<int:note_pk>", edit_note, name="edit note"),
    path("delete/<int:note_pk>", delete_note, name="delete note"),
    path("details/<int:note_pk>", note_details, name="note details"),
    path("profile/", profile, name="profile"),
    path("profile/delete/", delete_profile, name="delete profile"),
]

