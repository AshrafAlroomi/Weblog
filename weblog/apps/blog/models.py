from django.db import models
from weblog.apps.user.models import User
from weblog.utlis.article import STATUS_CHOICES, ACTIVE
from weblog.utlis.membership import MEMBERSHIP_STATUS, MEMBER_ROLE
from weblog.utlis.editor import EDITOR_PERMISSION


class BlogPreference(models.Model):
    default_publish_policy = models.CharField(max_length=10, choices=MEMBER_ROLE)
    default_membership_policy = models.CharField(max_length=10, choices=MEMBERSHIP_STATUS)
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

    def is_blog_editor(self, user):
        return self.admin == user


class EditorPermission(models.Model):
    permission = models.CharField(max_length=10, choices=EDITOR_PERMISSION, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)


class Editor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    permissions = models.ManyToManyField(EditorPermission)


class CategoryPreference(models.Model):
    style = models.JSONField()


class BlogBlackList(models.Model):  # todo
    pass
