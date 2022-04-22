from django.urls import path
from music_app.profiles.views import CreateProfileView, DeleteProfileView, ProfileDetailsView

urlpatterns = [
    path("create/", CreateProfileView.as_view(), name="create profile"),
    path("delete/", DeleteProfileView.as_view(), name="delete profile"),
    path("details/", ProfileDetailsView.as_view(), name="profile details"),
]
