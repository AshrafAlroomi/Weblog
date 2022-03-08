from django.db import models
from weblog.apps.user.models import User


class UserFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_follower")
    date = models.DateTimeField()
