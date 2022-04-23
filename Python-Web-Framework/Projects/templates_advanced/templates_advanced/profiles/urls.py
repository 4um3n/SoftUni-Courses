from django.urls import path
from templates_advanced.profiles.views import profile_details

urlpatterns = [
    path("", profile_details, name="profile details")
]
