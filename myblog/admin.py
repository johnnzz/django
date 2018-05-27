from django.contrib import admin
from myblog.models import Post, Category


# allow admin to manage Post, Category
admin.site.register(Post)
admin.site.register(Category)