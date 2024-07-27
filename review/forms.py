from django import forms
from .models import EReview
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class reviewForms(forms.ModelForm):
    class Meta:
        model = EReview
        fields = ['photo','movies_series_name','text','rating']

class UserRegeistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields = ('username','email','password1','password2')
        