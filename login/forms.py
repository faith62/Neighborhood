from django import forms
from .models import CustomUser,Profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model  =CustomUser
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighborhood')
