from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: 
        # This class provide a nested namespace for configurations and 
        # keep those configurations in a place.
        # What we have in the "field" will have in model too.
        # And the model affected here is model User.
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone','image'] 


# These code below are under constructing, purpose: Validate phone number input.
# class PhoneForm(forms.ModelForm):
#     class Meta:
#         model = PhoneModel
#         fields = ['phone']

