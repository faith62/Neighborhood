from django.forms import ModelForm,TextInput
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['image','title','description']

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['bsn_image','bsn_name','bsn_email','Category','weburl','phone']