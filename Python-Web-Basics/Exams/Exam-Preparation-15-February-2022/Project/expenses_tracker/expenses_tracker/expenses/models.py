from django.core.validators import MinValueValidator
from django.db import models

from expenses_tracker.profiles.models import Profile


class Expense(models.Model):
    title = models.CharField(
        max_length=30,
    )

    expense_image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(0),
        ],
    )

    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )
