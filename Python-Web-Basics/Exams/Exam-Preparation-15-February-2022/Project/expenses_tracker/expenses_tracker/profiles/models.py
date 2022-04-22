from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from expenses_tracker.profiles.validators import username_isalpha_validator, image_max_size_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            username_isalpha_validator,
        ]
    )

    last_name = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            username_isalpha_validator,
        ]
    )

    budget = models.FloatField(
        default=0,
        validators=[
            MinValueValidator(0),
        ]
    )

    profile_picture = models.ImageField(
        default="images/profile-pictures/default/user.png",
        upload_to="images/profile-pictures/",
        blank=True,
        validators=[
            image_max_size_validator,
        ]
    )

