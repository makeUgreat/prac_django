from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('prac_app:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('prac_app:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('prac_app:index')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prac_app:index')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html',context)

@login_required
def cancelAccount(request):
    request.user.delete()
    auth_logout(request)
    return redirect('prac_app:index')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('prac_app:index')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html',context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('prac_app:index')
    else:
        form = PasswordChangeForm(request.user)
    
    context ={
        'form': form,
    }
    return render(request,'accounts/change_password.html',context)