from django.db import models


class BookModel(models.Model):
    title = models.CharField(
        max_length=20,
    )
    pages = models.IntegerField(
        default=0,
    )
    description = models.CharField(
        max_length=100,
        default="",
    )
    author = models.CharField(
        max_length=20,
    )
