from django.forms import ModelForm,TextInput
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['image','title','description']