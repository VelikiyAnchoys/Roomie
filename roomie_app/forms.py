from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ad

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")




class PostForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['foto', 'title', 'category', 'prace', 'location', 'description', 'parking', 'contact']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'time': forms.HiddenInput(),
        }