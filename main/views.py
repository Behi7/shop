from django.shortcuts import render, redirect
from . import models
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def blogs(request):
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('index')
