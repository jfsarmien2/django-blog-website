from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post

all_posts = []


def get_date(post):
    return post["date"]

# Create your views here.


def blog_index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def blog_posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts": posts})


def blog_detail(request, slug):
    # blog_post = Post.objects.get(slug=slug)
    blog_post = get_object_or_404(Post, slug=slug)
    tags = blog_post.tags.all()
    return render(request, "blog/post-info.html", {"post": blog_post, "tags": tags})
