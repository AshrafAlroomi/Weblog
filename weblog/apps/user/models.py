from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    img = models.URLField()
    img_thumbnail = models.URLField()
    social_media = models.JSONField(null=True, blank=True)


class User(AbstractUser):
    name = models.TextField(max_length=100)
    profile = models.OneToOneField(Profile, null=True, on_delete=models.CASCADE)

