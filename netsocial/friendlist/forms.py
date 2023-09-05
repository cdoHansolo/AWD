from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm)
    email = forms.EmailField(max_length=254, required=True, help_text='Please enter a valid email address.')

    class Meta:
        model = User #built-in user model
        fields = ('username', 'email', 'password1', 'password2')