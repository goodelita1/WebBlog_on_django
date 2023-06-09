from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
    path("blog/create/", views.BlogCreate.as_view(), name="createpost"),
    path("blog/<int:pk>/update/", views.BlogUpdate.as_view(), name="updatepost"),
    path("blog/<int:pk>/delete/", views.BlogDelete.as_view(), name="deletepost"),
    path("blog/", views.BlogListPage.as_view(), name="bloglist"),
    path(
        "blog/<int:pk>/comments/", views.CommentListPage.as_view(), name="commentlist"
    ),
    path(
        "blog/<int:blog_id>/comments/create/",
        views.CommentCreate.as_view(),
        name="createcomment",
    ),
    path(
        "blog/comments/<int:pk>/update/",
        views.CommentUpdate.as_view(),
        name="updatecomment",
    ),
    path(
        "blog/comments/<int:pk>/delete/",
        views.CommentDelete.as_view(),
        name="deletecomment",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
