from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, CreateView , UpdateView , ListView
from main.models import BlogModel , CommentModel
# Create your views here.
class BlogCreate(CreateView):
    model = BlogModel
    fields = ['author', 'blog_text', 'blog_header', 'date']
    initial = {'author': 'faye valentine' , 'date': datetime.now() , 'blog_text': 'test_createview' , 'blog_header': 'test_blog_header'}
    template_name = 'blog/create_update_blog.html'  # Specify the template for rendering the form
    success_url = '/blog/'  # Specify the URL to redirect after successful form submission

class BlogUpdate(UpdateView):
    model = BlogModel
    fields = '__all__' # Not recommended (potential security issue if more fields added)
    template_name = 'blog/create_update_blog.html'  # Specify the template for rendering the form
    success_url = '/blog/'  # Specify the URL to redirect after successful form submission

class BlogDelete(DeleteView):
    model = BlogModel
    success_url = reverse_lazy('authors')
    template_name = 'blog/delete_blog.html'  # Specify the template for rendering the form
    success_url = '/blog/'  # Specify the URL to redirect after successful form submission
    
class BlogListPage(ListView):
    model = BlogModel
    context_object_name = 'blog'
    template_name='blog/blog_page.html'
    
class CommentCreate(CreateView):
    model = CommentModel
    fields = ['comment', 'comment_author', 'comment_time', 'comment_blog']
    initial = {'comment_author': 'faye valentine', 'comment_text': 'test_comment', 'comment_time': datetime.now() , 'comment_blog': BlogModel.blog_header}
    template_name = 'blog/create_update_comment.html'  # Specify the template for rendering the form
    
    def get_success_url(self):
        return reverse_lazy('blog:createcomment')
    
class CommentUpdate(UpdateView):
    model = CommentModel
    fields = '__all__' # Not recommended (potential security issue if more fields added)
    template_name = 'blog/create_update_comment.html'  # Specify the template for rendering the form
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:updatecomment', kwargs={'pk': pk})

class CommentDelete(DeleteView):
    model = CommentModel
    success_url = reverse_lazy('authors')
    template_name = 'blog/delete_comment.html'  # Specify the template for rendering the form
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:deletecomment', kwargs={'pk': pk})
    
class CommentListPage(ListView):
    model = BlogModel
    context_object_name = 'blog_comment'
    template_name = 'blog/comments_page.html'

    def get_queryset(self):
        pk = self.kwargs['pk']
        return get_object_or_404(BlogModel, pk=pk)

