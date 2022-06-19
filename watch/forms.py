from django.forms import ModelForm,TextInput
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio','name','neighborhood']

        def __init__(self, *args, **kwargs):
            super(ProfileUpdateForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()

class PostCreateForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['image','title','description']