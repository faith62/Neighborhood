
from django import forms
from .models import Neighbourhood,Posts,Profile,Business



class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['profile']
        fields='__all__'

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['profile','neig_id',]
        fields='__all__'

class EditProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        exclude = ['neighborhood','user']
        fields = '__all__'
