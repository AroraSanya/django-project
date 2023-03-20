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

class login_product(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password') 
