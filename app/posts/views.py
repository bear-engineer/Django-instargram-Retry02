from django.http import HttpResponse
from .models import Post
from django.shortcuts import render

def post(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return HttpResponse('post-list')
