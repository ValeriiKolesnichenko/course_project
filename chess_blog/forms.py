from django.forms import ModelForm, TextInput, Textarea, Select, PasswordInput, NumberInput
from .models import ChessPost, CustomUser, ChessComment, ChessCategory
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'rating', 'dignity']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
            }),
            'rating': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rating',
            }),
            'dignity': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Dignity',
            }),
        }


class AuthenticationFormWithPlaceholder(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))


class ChessPostForm(ModelForm):
    class Meta:
        model = ChessPost
        fields = ['title', 'content', 'category']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content',
            }),
            'category': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Category',
            })}


class ChessCommentForm(ModelForm):
    class Meta:
        model = ChessComment
        fields = ['content']
