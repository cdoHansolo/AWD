from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .models import FriendRequest
from .models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Please enter a valid email address.')

    class Meta:
        model = User #built-in user model
        fields = ('username', 'email', 'password1', 'password2')

    def clean_mail(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address is already used")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture','bio', 'birthday') 

class FriendRequestForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = []

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)