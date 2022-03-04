from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
)

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'bg-gray-100 rounded-lg p-2'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'bg-gray-100 rounded-lg p-2',
        }
    ))


class UserSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "bg-gray-100 rounded-lg p-2"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "bg-gray-100 rounded-lg p-2",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "bg-gray-100 rounded-lg p-2",
            }
        )
    )
