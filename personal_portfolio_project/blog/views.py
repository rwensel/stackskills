from django.shortcuts import render
from .models import BlogPost


def all_blogs(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/all_blogs.html', {'blog_posts': blog_posts})
