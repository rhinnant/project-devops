# login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # rename import
from django.contrib import messages

def user_login(request):  # renamed to user_login
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # use renamed auth_login
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login/login.html')

