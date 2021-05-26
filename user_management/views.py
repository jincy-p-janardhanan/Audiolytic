from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *
from .models import *

import logging

class AudioUploadView(CreateView):
    model = UploadAudio
    fields = ['uploaded_file', ]
    success_url = reverse_lazy('download')
    logging.debug('in view')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uploaded_files = UploadAudio.objects.all()
        if uploaded_files == None:
            logging.debug("No objects received")
        else:
            logging.debug('got objects', context)
        context['uploaded_file'] = uploaded_files
        logging.info('returning context', context)
        return context

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
        return redirect('/upload')
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
def download(request):
    return render(request, 'file_download.html')

def index(request):
    return render(request, 'home.html')

# @login_required
# def browse(request):
#     return render(request, 'filebrowser.html')