from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from main.models import BlogModel, CommentModel
from django.core.mail import EmailMessage


# Create your views here.
class BlogCreate(LoginRequiredMixin, CreateView):
    model = BlogModel
    fields = ["blog_text", "blog_header", "date", "is_hidden", "blog_image"]
    initial = {
        "date": datetime.now(),
        "blog_text": "test_createview",
        "blog_header": "test_blog_header",
    }
    template_name = "blog/create_blog.html"
    success_url = "/blog/"

    def form_valid(self, form):
        form.instance.blog_author = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        recipient_email = "goodelita1@gmail.com"
        subject = request.POST.get("blog_header")
        message_text = request.POST.get("blog_text")
        user_name = self.request.user
        message = str(message_text) + "    " + str(user_name)
        email = EmailMessage(subject, message, to=[recipient_email])
        email.send()
        return self.form_valid(self.get_form())


class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogModel
    fields = ["blog_text", "blog_header", "date", "is_hidden", "blog_image"]
    template_name = "blog/update_blog.html"
    success_url = "/blog/"

    def test_func(self):
        blog = self.get_object()
        return (
            self.request.user.is_superuser
            or self.request.user == self.get_object().blog_author
        )


class BlogDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogModel
    success_url = reverse_lazy("authors")
    template_name = "blog/delete_blog.html"
    success_url = "/blog/"

    def test_func(self):
        blog = self.get_object()
        return (
            self.request.user.is_superuser
            or self.request.user == self.get_object().blog_author
        )


class BlogListPage(ListView):
    model = BlogModel
    context_object_name = "blog"
    template_name = "blog/blog_page.html"


class CommentCreate(LoginRequiredMixin, CreateView):
    model = CommentModel
    fields = ["comment"]
    initial = {"comment_text": "test_comment"}
    template_name = "blog/create_comment.html"

    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        blog = get_object_or_404(BlogModel, id=self.kwargs["blog_id"])
        form.instance.comment_blog = blog
        form.instance.comment_time = datetime.now()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        recipient_email = BlogModel.objects.get(id=self.kwargs["blog_id"])
        gmail = recipient_email.blog_author.email
        subject = datetime.now()
        message_text = request.POST.get("comment")
        user_name = self.request.user
        message = str(message_text) + "    " + str(user_name)
        email = EmailMessage(subject, message, to=[gmail])
        email.send()
        return self.form_valid(self.get_form())

    def get_success_url(self):
        return reverse_lazy("blog:commentlist", kwargs={"pk": self.kwargs["blog_id"]})


class CommentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CommentModel
    fields = ["comment"]
    template_name = "blog/update_comment.html"

    def get_success_url(self):
        blog_id = self.object.comment_blog_id
        return reverse("blog:commentlist", kwargs={"pk": blog_id})

    def test_func(self):
        comment = self.get_object()
        return (
            self.request.user.is_superuser
            or self.request.user == comment.comment_author
        )


class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CommentModel
    success_url = reverse_lazy("authors")
    template_name = "blog/delete_comment.html"

    def get_success_url(self):
        blog_id = self.object.comment_blog_id
        return reverse("blog:commentlist", kwargs={"pk": blog_id})

    def test_func(self):
        comment = self.get_object()
        return (
            self.request.user.is_superuser
            or self.request.user == comment.comment_author
        )


class CommentListPage(ListView):
    model = BlogModel
    context_object_name = "blog_comment"
    template_name = "blog/comments_page.html"

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return get_object_or_404(BlogModel, pk=pk)
