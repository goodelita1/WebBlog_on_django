from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from main.models import BlogModel
from .forms import SignUpForm
from django.views.generic import CreateView, UpdateView, ListView
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("users:login")
    template_name = "users/signup.html"


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy("blog:bloglist")
    template_name = "users/profile.html"


class LogOutView(LogoutView):
    http_method_names = ["get", "post", "options"]
    next_page = reverse_lazy("blog:bloglist")


class LogInView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("blog:bloglist")

    def get_success_url(self):
        return reverse_lazy("blog:bloglist")


class HiddenPost(LoginRequiredMixin, ListView):
    model = BlogModel
    context_object_name = "hidden"
    template_name = "users/hidden_posts.html"

    def get_queryset(self):
        return BlogModel.objects.filter(blog_author=self.request.user)


class MyPosts(LoginRequiredMixin, ListView):
    model = BlogModel
    context_object_name = "myposts"
    template_name = "users/my_posts.html"

    def get_queryset(self):
        return BlogModel.objects.filter(blog_author=self.request.user)
