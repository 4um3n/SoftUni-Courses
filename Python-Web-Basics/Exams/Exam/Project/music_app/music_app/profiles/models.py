from django.db import models
from django.core.validators import MinLengthValidator
from music_app.profiles.validators import username_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            username_validator,
        ],
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
