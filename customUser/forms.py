from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['first_name','last_name','username','email','types','sex','location','password1','password2']


class UserChangeForm(UserChangeForm):
    class Meta:
        model=User
        fields=['image','username','email','location','bio']