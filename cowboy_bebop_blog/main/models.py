from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class BlogModel(models.Model):
    blog_author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_header = models.CharField(max_length=50)
    blog_text = models.TextField()
    date = models.DateTimeField()
    blog_image = models.ImageField(upload_to="image", blank=True, null=True)
    is_hidden = models.BooleanField(default=False, verbose_name="Make it Hidden?")

    def get_absolute_url(self):
        return reverse("blog:bloglist", kwargs={"pk": self.pk})

    def __str__(self):
        return self.blog_header

    class Meta:
        ordering = ["blog_header"]


class CommentModel(models.Model):
    comment = models.TextField()
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_time = models.DateTimeField()
    comment_blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("blog:commentlist", kwargs={"pk": self.pk})

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["comment_author"]
