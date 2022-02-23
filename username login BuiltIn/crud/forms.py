from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import user



class Sregistration(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'})
        }


class Uregistration(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        #fields= '__all__'
        fields = ['first_name','last_name','username','email', 'password1','password2']

        
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        # }
        