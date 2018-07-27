from django.shortcuts import render

# Create your views here.
'''''
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

'''''
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
<<<<<<< HEAD
from boards.forms import SignUpForm

def home(request):
    return render(request,'home.html')
=======

from boards.forms import SignUpForm
>>>>>>> 966fae0f6f5c6eaa8497c6eeefa095d8cef396d1

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,'hello.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})