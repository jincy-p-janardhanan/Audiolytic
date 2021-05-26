from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import *

import logging

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'file_upload.html', {
        'form': form
    })

def signup(request):
    if request.user.is_authenticated:
        return render(request, 'file_upload.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            logging.debug('form valid')
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return redirect(request, '/upload')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logging.debug(user)
            return redirect('/upload')
        else:
            form = AuthenticationForm(request.POST)
            logging.debug('Received user None')
            return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    return redirect('/')

@login_required
def upload(request):
    return render(request, 'file_upload.html')

@login_required
def download(request):
    return render(request, 'file_download.html')

def index(request):
    return render(request, 'home.html')

@login_required
def browse(request):
    return render(request, 'filebrowser.html')