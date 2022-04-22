from django.urls import path
from expenses_tracker.profiles.views import ProfileDetailsView, EditProfileView, ProfileDeleteView
# profile_details, profile_edit, profile_delete
from expenses_tracker.profiles import signals

urlpatterns = [
    path("", ProfileDetailsView.as_view(), name="profile details"),
    path("edit/", EditProfileView.as_view(), name="profile edit"),
    path("delete/", ProfileDeleteView.as_view(), name="profile delete"),
]
