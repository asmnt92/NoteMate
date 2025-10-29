from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout




def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')

        errors = []  

        # Password check
        if password != confirm_password:
            errors.append('Passwords don\'t match')

        # Username already exists check
        if User.objects.filter(username=username).exists():
            errors.append('Username already exists')

        # Email already exists check
        if User.objects.filter(email=email).exists():
            errors.append('Email already exists')

        # if errors
        if errors:
            for err in errors:
                messages.error(request, err)
            return redirect('users:sign-up')  

        # User create (with hashed password) and save in data base
        User.objects.create_user(username=username, email=email, password=password)
        

        messages.success(request, 'User created successfully!')
        return redirect('users:sign-in')
        

    return render(request, 'home.html')




def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Username check
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('users:sign-in')  

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('notes:notes')  
        else:
            messages.error(request, 'Incorrect password')
            return redirect('users:sign-in')

    return render(request, 'home.html')

def sign_out(request):
    
    logout(request)

    return redirect('home:guest-page')
