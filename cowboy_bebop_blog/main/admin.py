from django.contrib import admin
from .models import BlogModel, CommentModel


# Register your models here.
@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("blog_header", "blog_author", "date", "blog_image")
    list_filter = ("date", "blog_header")
    search_fields = ("blog_text__startswith",)


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "comment_author", "comment_time")
    list_filter = ("comment_time", "comment_author")
    search_fields = ("comment__startswith",)
