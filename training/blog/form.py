from django import forms
from blog.models import Blog
from django.contrib.auth.models import User

class RegisterForms(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email')

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields ='__all__'

class Login_form(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password')       