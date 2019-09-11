from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, UserPasswordChange

def home(request):
    return render(request, 'pages/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been Looged In.'))
            return redirect('home')
        else:
            messages.success(request, ('Error Logging In, Please Try Again or contact the course administrator.'))
            return redirect('login')
    else:
        return render(request, 'pages/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been Looged Out.'))
    return render(request, 'pages/login.html', {})

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, ('The user has been created'))
            return redirect('register')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'pages/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Profile Edited'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form':form}
    return render(request, 'pages/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChange(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('Password Edited'))
            return redirect('home')
    else:
        form = UserPasswordChange(user=request.user)
    context = {'form':form}
    return render(request, 'pages/change_password.html', context)
