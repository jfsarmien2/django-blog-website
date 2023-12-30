from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="starting-page"),
    path("posts", views.blog_posts, name="posts-page"),
    path("posts/<slug:slug>", views.blog_detail, name="post-info-page")
]
