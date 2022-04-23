from django.db import models
from petstagram.accounts.models import UserProfile


class Pet(models.Model):
    CHOICE_TYPE_DOG = 'dog'
    CHOICE_TYPE_CAT = 'cat'
    CHOICE_TYPE_PARROT = 'parrot'
    TYPE_CHOICES = (
        (CHOICE_TYPE_DOG, 'Dog'),
        (CHOICE_TYPE_CAT, 'Cat'),
        (CHOICE_TYPE_PARROT, 'Parrot'),
    )

    user = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.ImageField(upload_to="images")

    def __str__(self):
        return f"{self.name}({self.pk})"


class Like(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.pet.name}"


class Comment(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
    )
    comment = models.TextField()
