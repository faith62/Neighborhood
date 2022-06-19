from multiprocessing import context
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from watch.models import Posts
from .decorators import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail,BadHeaderError


def homepage(request):
    posts = Posts.objects.all().order_by('id').reverse()
    context={
        'posts':posts
    }
    return render(request,'watch/index.html',context=context)

def post_create(request):
    post_create_form = PostCreateForm()

    if request.method == "POST":
        post_create_form = PostCreateForm(request.POST,request.FILES)
        if post_create_form.is_valid():
            post_user = request.user
            
            image = post_create_form.cleaned_data.get('image')
            title = post_create_form.cleaned_data.get('title')
            description = post_create_form.cleaned_data.get('description')
            profile = Profile.objects.get(user=post_user)
            
            new_post = Posts(
                image=image,
                title=title,
                description=description,
                profile=profile
            )
            new_post.save_post()
            return redirect('homepage')

    context={
        'post_create_form':post_create_form
    }
    return render(request,'watch/post_create.html',context=context)

def police(request):
    police_station=Business.objects.filter(category='Police Station')
    context={'police_station':police_station}
    return render(request,'amenities/police.html',context=context)