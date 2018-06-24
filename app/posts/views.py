from django.http import HttpResponse
from django.shortcuts import render

def post(request):
    return HttpResponse('post-list')
