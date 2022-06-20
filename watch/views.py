from django.shortcuts import redirect, render
from django.urls import resolve
from .models import Neighbourhood,Profile,Posts,Business

from .forms import PostForm

from django.shortcuts import get_object_or_404, render,redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    
    homes = Neighbourhood.objects.all()

    return render(request, 'index.html',{'homes':homes,})

def viewhood(request, pk):
    homes= Neighbourhood.objects.get(id=pk)
    posts = Posts.objects.all()
   
    return render(request, 'single_hood.html',{'homes':homes,'posts':posts})

def new_post(request):
    current_user = request.user
    # homes= Neighbourhood.objects.get(id=home_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
        return redirect('home')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})

def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    

    return render(request,'profile.html',{ 'profile':profile,})

#auth
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
