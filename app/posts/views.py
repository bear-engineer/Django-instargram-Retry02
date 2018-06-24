from django.http import HttpResponse
from .models import Post
from django.shortcuts import render

def post(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/post_list.html', context)
