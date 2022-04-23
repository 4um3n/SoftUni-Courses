from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from petstagram.accounts.views import sign_up, user_profile_details
from petstagram.accounts import signals

urlpatterns = [
    path("", include(auth_urls)),
    path("signup/", sign_up, name="sign up"),
    path("profile/", user_profile_details, name="user profile details"),
]
