from django.db import models
from weblog.apps.user.models import User
from weblog.apps.blog.models import Blog
from weblog.utlis.membership import MEMBERSHIP_STATUS, MEMBER_ROLE, NON


class UserFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_follower")
    date = models.DateTimeField()


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=10, choices=MEMBER_ROLE, default=NON)
    join_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=MEMBERSHIP_STATUS)


class BlogFollow(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_follower")
    date = models.DateTimeField(auto_now=True)
