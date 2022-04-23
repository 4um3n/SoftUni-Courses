from django.db import models
from django.contrib.auth.models import AbstractUser
from templates_advanced.pythons_auth.models import PythonsUser


class Profile(models.Model):
    picture = models.URLField(
        blank=True
    )
    website = models.URLField(
        blank=True
    )
    description = models.TextField(
        blank=True,
        max_length=150
    )
    is_complete = models.BooleanField(
        default=False
    )

    user = models.OneToOneField(
        PythonsUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f"{self.user.username}"
