from django.db import models
from django.core.validators import MinValueValidator
from music_app.profiles.models import Profile


class Album(models.Model):
    POP_CHOICE = "Pop Music"
    JAZZ_CHOICE = "Jazz Music"
    R_AND_B_CHOICE = "R&B Music"
    ROCK_CHOICE = "Rock Music"
    COUNTRY_CHOICE = "Country Music"
    DANCE_CHOICE = "Dance Music"
    HIP_HOP_CHOICE = "Hip Hop Music"
    OTHER_CHOICE = "Other"

    GENRE_CHOICES = (
        (POP_CHOICE, "Pop Music"),
        (JAZZ_CHOICE, "Jazz Music"),
        (R_AND_B_CHOICE, "R&B Music"),
        (ROCK_CHOICE, "Rock Music"),
        (COUNTRY_CHOICE, "Country Music"),
        (DANCE_CHOICE, "Dance Music"),
        (HIP_HOP_CHOICE, "Hip Hop Music"),
        (OTHER_CHOICE, "Other"),
    )

    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[
            MinValueValidator(0)
        ],
    )

    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )
