from django.shortcuts import render
from .models import BlogModel
from django.views.generic import ListView

# Create your views here.
class BlogList(ListView):
    model = BlogModel
    context_object_name = 'blog'
    template_name='main/main_page.html'