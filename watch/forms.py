
from django import forms
from .models import Neighbourhood,Posts



class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['profile']
        fields='__all__'
        