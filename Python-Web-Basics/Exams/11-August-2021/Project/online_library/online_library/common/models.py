from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    image_url = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(
        max_length=30,
    )
    description = models.CharField(
        max_length=30,
    )
    image = models.URLField()
    book_type = models.CharField(
        max_length=30,
    )
    added_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} added by {self.added_by}"
