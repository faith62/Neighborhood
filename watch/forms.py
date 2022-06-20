
from django import forms
from .models import Neighbourhood,Posts,Profile



class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['profile']
        fields='__all__'

class EditProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        exclude = ['neighborhood','user']
        fields = '__all__'
