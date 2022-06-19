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
    posts = Posts.objects.all()
    context={
        'posts':posts
    }
    return render(request,'watch/index.html',context=context)