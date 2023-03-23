from django import forms
from .models import * 
from django.contrib.auth.models import User
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'


class RegisterForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Username'
                }),
                 'password': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                 }),
                # 'email': forms.EmailInput(attrs={
                # 'class': "form-control",
                # 'placeholder': 'Email'
                # }),
        }

class login_product(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password') 
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Username'
                }),
                 'password': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': 'Password'
                 }),
        }

class 

