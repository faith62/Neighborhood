from django.shortcuts import redirect, render
from django.urls import resolve
from .models import Neighbourhood,Profile,Posts,Business

from .forms import PostForm,EditProfileForm,BusinessForm

from django.shortcuts import get_object_or_404, render,redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from django.core.paginator import Paginator
# Create your views here.
def home(request):
    
    homes = Neighbourhood.objects.all()

    return render(request, 'index.html',{'homes':homes,})

def viewhood(request, pk):
    homes= Neighbourhood.objects.get(id=pk)
    posts = Posts.objects.all().filter(neighborhood_id=pk)
    businesses = Business.objects.all()
   
    return render(request, 'single_hood.html',{'homes':homes,'posts':posts,'businesses':businesses})

# def viewbuss(request, pk):
#     homes= Neighbourhood.objects.get(id=pk)
#     businesses = Business.objects.all().filter(neig_id_id=pk)
    
#     return render(request, 'business.html',{'businesses':businesses,'homes':homes,})

def new_post(request):
    current_user = request.user
    # homes= Neighbourhood.objects.get(id=homes_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            # post.neighborhood = homes
            post.save()
            
        return redirect('home')

    else:
        form = PostForm()

    return render(request, 'new_post.html', {"form": form,})

def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.all().filter(user=user)
    url_name= resolve(request.path).url_name

    if url_name == "profile":
        posts =Posts.objects.filter(user=user)
    
    #Paginator
    paginator = Paginator(posts,8)
    page_number = request.GET.get('page')
    posts_paginator= paginator.get_page(page_number)

    return render(request,'profile.html',{ 'profile':profile,'posts':posts_paginator,  'url_name':url_name,})

def EditProfile(request):
	user = request.user.id
	profile = Profile.objects.all().filter(user__id=user)
	

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile = form.save()
			profile.save()
			return redirect('home')

	else:
		form = EditProfileForm()

	
	return render(request, 'edit_profile.html', {'form':form,})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('login')

    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def new_business(request):
    current_user = request.user
    # homes= Neighbourhood.objects.get(id=homes_id)

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.editor = current_user
            # business.neig_id = homes
            business.save()
        return redirect("home")

    else:
        form = BusinessForm()

    return render(request, 'new_business.html', {"form": form,})

# def new_post(request,homes_id):
#     current_user = request.user
#     homes= Neighbourhood.objects.get(id=homes_id)

#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.editor = current_user
#             post.neighborhood = homes
#             post.save()
#         return redirect('singlehood',homes_id)

#     else:
#         form = PostForm()

#     return render(request, 'new_post.html', {"form": form,})
