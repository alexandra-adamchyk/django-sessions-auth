from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import LoginForm


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) # sessions are saved automated 
                return redirect(reverse_lazy('dashboard'))
            else:
                return render(request, 'users/login2.html', {'form': form, 'error': 'Invalid password or username'})
        
    return render(request, 'users/login2.html', {'form': form, 'error': None})


@login_required
def dashboard(request):    
    return render(request, 'users/dashboard.html')


def logout_view(request):
    logout(request) # removes the session related to authentication
    return redirect(reverse_lazy('login_view'))