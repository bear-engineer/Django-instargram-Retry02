from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:post-list')
        else:
            return redirect('members:sign-in')
    else:
        return render(request, 'members/sign_in.html')

def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password == password2:
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password2,)
            user = authenticate(request, username=username, password=password2)
            login(request, user)
            return redirect('posts:post-list')
        else:
            return redirect('members:sign-up')
    else:
        return render(request,'members/sign_up.html')