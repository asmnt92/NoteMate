from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.
# def sign_up(request):
#     if request.method == 'POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         confirm_password=request.POST.get('confirm_password')
#         email=request.POST.get('email')
#         if password == confirm_password:
#             errors=[]
#             if User.objects.filter(username=username).exists():
#                 errors.append('Username already exists')
#             elif User.objects.filter(email=email).exists():
#                 errors.append('Email already exists')
#             else:
#                 # user create with hashed password
#                 User.objects.create_user(username=username, email=email, password=password)
#                 messages.success(request, 'User created successfully')
               
#         else:
#             errors.append('Passwords do not match')

        
#     return render(request,'sign-up.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')

        errors = []  # সব error এখানে collect হবে

        # Password check
        if password != confirm_password:
            errors.append('Passwords don\'t match')

        # Username already exists check
        if User.objects.filter(username=username).exists():
            errors.append('Username already exists')

        # Email already exists check
        if User.objects.filter(email=email).exists():
            errors.append('Email already exists')

        # যদি error থাকে → সবগুলো দেখাবে
        if errors:
            for err in errors:
                messages.error(request, err)
            return redirect('users:sign-up')  # error হলে একই পেজে ফেরত পাঠানো

        # User create (with hashed password)
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'User created successfully!')
        return redirect('users:sign-in')
        

    return render(request, 'sign-up.html')




def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Username check
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('users:sign-in')  # নিজের app-এর namespace

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome {user.username} 👋')
            return redirect('notes:notes')  # অন্য app এ redirect
        else:
            messages.error(request, 'Incorrect password')
            return redirect('users:sign-in')

    return render(request, 'sign-in.html')

def sign_out(request):
    
    logout(request)

    return redirect('home:guest-page')
