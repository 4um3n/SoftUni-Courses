from django.db import models


class Object(models.Model):
    name = models.CharField(
        max_length=10
    )
    image = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    weight = models.FloatField()


class Post(models.Model):
    title = models.CharField(
        max_length=30
    )
    description = models.TextField(
        max_length=500
    )
    author_name = models.CharField(
        max_length=10
    )
    author_phone = models.CharField(
        max_length=10
    )
    found = models.BooleanField(
        default=False
    )
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
