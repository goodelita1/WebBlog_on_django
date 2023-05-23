from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("blog/sign_up/", views.SignUpView.as_view(), name="signup"),
    path("blog/log_in/", views.LogInView.as_view(), name="login"),
    path("blog/profile/<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path("blog/log_out/", views.LogOutView.as_view(), name="logout"),
    path("blog/hidden_post", views.HiddenPost.as_view(), name="hiddenpost"),
    path("blog/my_posts", views.MyPosts.as_view(), name="myposts"),
]
