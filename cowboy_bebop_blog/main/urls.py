from django.urls import path
from . import views

app_name = "main"

urlpatterns = [path("main/", views.BlogList.as_view(), name="main")]
