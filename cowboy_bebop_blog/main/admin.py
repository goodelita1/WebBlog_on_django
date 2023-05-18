from django.contrib import admin
from .models import BlogModel ,CommentModel

# Register your models here.
@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    pass