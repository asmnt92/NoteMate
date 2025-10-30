from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator




def sign_up(request):
    url=reverse('home:guest-page')
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
        user=User(username=username, email=email,is_active=False)
        user.set_password(password)
        user.save()
        print(user)
        messages.success(request, 'Account created! Please verify your email before login.')


        
        return redirect(f"{url}?signIn=True")
    
    return redirect(f"{url}?signUp=True")

    




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
            return render(request, 'home.html',{'signIn':True})

    url=reverse('home:guest-page')
    return redirect(f"{url}?signIn=True")

def sign_out(request):
    logout(request)
    url=reverse('home:guest-page')
    return redirect(f"{url}?signIn=True")


def activate_user(request,id,token):
    try:
        user=User.objects.get(id=id)
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()

            url=reverse('home:guest-page')
            return redirect(f"{url}?signIn=True")
        else:
            return HttpResponse('Invalid token')
        
    except User.DoesNotExist:
        return HttpResponse('User not found')
