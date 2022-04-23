from django.contrib.auth.models import User
from django.db import models

from petstagram.accounts.services import get_profile_pictures_directory


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    profile_picture = models.ImageField(
        upload_to=get_profile_pictures_directory(
            filename=str(user)
        ),
        default="No Image",
    )
