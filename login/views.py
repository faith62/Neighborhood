from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render,redirect
from django.contrib.auth.backends import RemoteUserBackend
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignupForm()
#     return render(request, 'registration/signup.html', {'form': form})

# Create your views here.
# csrf_exempt
# @login_required
# def profile(request):
#     title = 'Your Profile Information'
#     if request.method == 'POST':
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return redirect('hood')
#     else:
#         user_form = UserUpdateForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.profile)
#         context = {
#             'title': title,
#             'user_form': user_form,
#             'profile_form': profile_form,
#         }
#         return render(request, 'profile.html', context)

csrf_exempt
@login_required
def ProfileDetail(request):
    current_user = request.user
    return render(request, 'profile_details.html', {'current_user': current_user})
