from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def signup(request):
    form = SignupForm(request.POST)
