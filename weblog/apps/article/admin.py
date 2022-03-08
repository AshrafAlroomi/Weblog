from django.contrib import admin
from .models import Article, ArticleImage, EditHistory, Comment, Reply
# Register your models here.
admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(EditHistory)
admin.site.register(Comment)
admin.site.register(Reply)
