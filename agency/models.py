from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experiments = models.IntegerField(default=0)

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1024)
    published_date = models.DateTimeField()
    topic = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="newspapers")

    class Meta:
        ordering = ("published_date",)
