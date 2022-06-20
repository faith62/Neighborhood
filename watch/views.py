from django.shortcuts import redirect, render
from django.urls import resolve
from .models import Neighbourhood,Profile,Posts,Business

from .forms import PostForm,EditProfileForm

from django.shortcuts import get_object_or_404, render,redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.
def home(request):
    
    homes = Neighbourhood.objects.all()

    return render(request, 'index.html',{'homes':homes,})

def viewhood(request, pk):
    homes= Neighbourhood.objects.get(id=pk)
    posts = Posts.objects.all()
   
    return render(request, 'single_hood.html',{'homes':homes,'posts':posts})

def new_post(request,homes_id):
    current_user = request.user
    homes= Neighbourhood.objects.get(id=homes_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
        return redirect('singlehood',homes_id)

    else:
        form = PostForm()

    return render(request, 'new_post.html', {"form": form,'homes':homes})

def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    # profile = Profile.objects.all()

    return render(request,'profile.html',{ 'profile':profile,})
def EditProfile(request):
	user = request.user.id
	profile = Profile.objects.get(user__id=user)
	BASE_WIDTH = 400

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES)
		if form.is_valid():
			
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
            return redirect('/login')

    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})
