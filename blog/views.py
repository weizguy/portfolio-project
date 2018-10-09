from django.shortcuts import render, get_object_or_404

from .models import Blog

def posts(req):
    posts = Blog.objects
    return render(req, 'blog/posts.html', {'posts':posts})

def detail(req, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(req, 'blog/detail.html', {'post':post})

    