from pyexpat import model
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class signUpForm(UserCreationForm):
      password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
      class Meta:
            model =User
            fields = ['username','first_name','last_name','email']
            labels ={'email':'Email'}

class editUserForm(UserChangeForm):
      password= None
      class Meta:
            model=User
            fields =['username','first_name','last_name','email']
            labels ={'email':'email'}

class editAdminForm(UserChangeForm):
      password= None
      class Meta:
            model=User
            fields ='__all__'
            labels ={'email':'email'}