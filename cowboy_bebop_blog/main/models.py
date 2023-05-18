from django.db import models
from django.urls import reverse

# Create your models here.
class BlogModel(models.Model):
    author = models.CharField(max_length=50)
    blog_header = models.CharField(max_length=50)
    blog_text = models.TextField()
    date = models.DateTimeField()
    
    def get_absolute_url(self):
        return reverse("blog:bloglist", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.blog_header
    
    class Meta:
        ordering = ['blog_header']

class CommentModel(models.Model):
    comment = models.TextField()
    comment_author = models.CharField(max_length=50)
    comment_time = models.DateTimeField()
    comment_blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')
    
    def get_absolute_url(self):
        return reverse("blog:commentlist", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.comment_author
    
    class Meta:
        ordering = ['comment_author']
    