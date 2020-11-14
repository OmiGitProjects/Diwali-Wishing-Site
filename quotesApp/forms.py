from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, UserChangeForm
from django.contrib.auth.models import User
from .models import QuotesDatabase

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Type Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password (Again)", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Type Any Username',
            'first_name': 'Type Your First Name',
            'last_name': 'Type Your Last Name',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),  
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')

        if len(username) <= 3 or len(username) > 15:
            raise forms.ValidationError("Type More than 3 Characters!!!")
        if len(first_name) <= 3 or len(first_name) >= 10:
            raise forms.ValidationError("Type More than 3 Characters!!!")
        if len(last_name) <= 3 or len(last_name) >= 20:
            raise forms.ValidationError("Type More than 3 Characters!!!")

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Enter Your Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Enter Your Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AddWishesForm(forms.ModelForm):
    class Meta:
        model = QuotesDatabase
        fields = ['quote']
        labels = {
            'quote': 'Type Your Diwali Wish',
        }
        widgets = {
            'quote': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomPasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Type New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Your Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'date_joined', 'last_login']
        labels = {
            'first_name': 'Your First Name',
            'last_name': 'Your Last Name',
        }