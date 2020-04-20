from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register_user(request):
    if request.user.is_authenticated:
        return redirect('landing_page')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('landing_page')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/register.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('landing_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landing_page')

    return render(request, 'authentication/login.html')

def logout_user(request):
    logout(request)
    return redirect('landing_page')
