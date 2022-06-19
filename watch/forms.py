from django.forms import ModelForm,TextInput
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PostCreateForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['image','title','description']