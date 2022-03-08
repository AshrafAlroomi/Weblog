from django.db import models
from weblog.apps.user.models import User
from weblog.utlis import STATUS_CHOICES, ACTIVE


class BlogPreference(models.Model):
    publish_policy = models.TextField(max_length=100)  # todo
    membership_policy = models.TextField(max_length=100)  # todo
    style = models.JSONField()

    def set_membership_policy(self):
        pass


class Category(models.Model):
    name = models.TextField(max_length=10)
    style = models.OneToOneField(BlogPreference, on_delete=models.CASCADE)


class Blog(models.Model):
    name = models.TextField(max_length=20, unique=True)
    url = models.TextField(max_length=15, unique=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    style = models.OneToOneField(BlogPreference, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_default_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)

    def is_blog_owner(self, user):
        if self.admin == user:
            return True
        return False

    def can_post(self, user):
        if self.style.membership_policy == '':
            pass
        return False

    def is_blog_editor(self, user):
        return self.admin == user


class Editor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    permissions = models.TextField(max_length=20)  # todo


class CategoryPreference(models.Model):
    style = models.JSONField()


class BlogBlackList(models.Model):
    pass
