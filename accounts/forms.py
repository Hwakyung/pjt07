from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms
from .models import User
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Email address'),
                'required': 'True',
            }
        )
    )
    first_name = forms.CharField(
        label=('first_name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('first_name'),
                'required': 'True',
            }
        )
    )
    last_name = forms.CharField(
        label=('last_name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('last_name'),
                'required': 'True',
            }
        )
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

# class UserCreationForm(forms.ModelForm):
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ('__all__',email, first_name,last_name)