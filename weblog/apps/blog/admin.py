from django.contrib import admin
from .models import Blog, BlogPreference, Category, Editor, CategoryPreference

admin.site.register(Blog)
admin.site.register(BlogPreference)
admin.site.register(Category)
admin.site.register(Editor)
admin.site.register(CategoryPreference)
