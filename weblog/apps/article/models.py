from django.db import models
from weblog.apps.blog.models import Blog
from weblog.apps.user.models import User
from weblog.utlis.article import STATUS_CHOICES


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=100)
    subtitle = models.TextField(max_length=100)
    img = models.URLField()
    img_thumbnail = models.URLField()
    body = models.TextField(max_length=3000)
    blog = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def prepare_article(self):
        pass

    def author_edit(self):
        pass

    def editor_edit(self):
        pass

    @property
    def in_blog(self):
        if self.blog:
            return True
        return False


class EditHistory(models.Model):
    STATUS_CHANGE = "STATUS"
    AUTHOR_EDIT = "AUTHOR_UPDATE"
    EDIT_TYPES = STATUS_CHOICES = (
        (STATUS_CHANGE, "STATUS"),
        (AUTHOR_EDIT, "AUTHOR_UPDATE")
    )

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    type = models.CharField(max_length=14, choices=EDIT_TYPES)


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    img = models.URLField()
    place = models.IntegerField(default=0)
    index = models.IntegerField(default=0)
    type = models.TextField(max_length=10)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField(max_length=100)
    date = models.DateTimeField()

    def handle(self):
        pass

    def is_mine(self, user):
        if self.user == user:
            return True
        return False


class Reply(models.Model):
    user = models
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def handle(self):
        pass

    def is_mine(self, user):
        if self.user == user:
            return True
        return False
