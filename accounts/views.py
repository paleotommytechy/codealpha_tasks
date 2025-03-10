from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        
        #Validate passwords
        if password1 != password2:
            messages.error(request,'Passwords do not match')
            return redirect('accounts:register')
        
        #Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('accounts:register')
        
        #Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('accounts:register')
        
        #Create and save user
        user = User.objects.create_user(username=username,email=email, password=password1)
        user.save()

        messages.success(request, 'Registration Successful! You can now log in.')
        return redirect('accounts:login')
    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Login Successful!')
            return redirect('shop:homepage')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'You have been logged out.')
    return redirect('accounts:login')

