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

class order_form(forms.ModelForm):
    class Meta:
        model=Order
        fields=('address','product','total_cost','user_id') 
        # widgets = {
        #     'order_id': forms.TextInput(attrs={
        #         'class': "form-control",
        #         'placeholder': 'Username'
        #         }),
        # }

class AddressForm(forms.ModelForm):
    class Meta:
        model =AddressModel
        fields = ('name','address1','address2','zip_code','city')
        widgets ={
            'name':forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Address'
                }),
                'address1': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'address'
                }),
                'address2':forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'address'
                }),
                'zipcode':forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'zip code'
                }),
                'city':forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'city'
                }),
        }
               

# class profileForms(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput())
#     email=forms.TextInput()
#     widgets = {
#             'username': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Username'
#                 }),
#                  'password': forms.PasswordInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Password'
#                  }),
#                 'email': forms.EmailInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Email'
#                 }), 
#                 }              




