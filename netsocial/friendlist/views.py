from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import UserProfile

from .forms import RegisterForm
from .forms import EditProfileForm

# Create your views here

def home_view(request):
    return render(request, 'friendlist/homepage.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already in use.')
                return render(request, 'friendlist/register_form.html', {'form': form})
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user) #login the new user
            return redirect('profile') #Redirect to user's profile
    else:
        form = RegisterForm()
    return render(request, 'friendlist/register_form.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile') #Redirect to user's profile
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'friendlist/loginpage.html', {'form': form})

def profile_view(request):
    user = request.user #user successfully login
    context = {
                'user': user,
              }
    return render(request, 'friendlist/profilepage.html', context)

def edit_profile_view(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']

            user_profile.bio = bio
            user_profile.birthday = birthday
            user_profile.save()

            return redirect('profile') #redirect back to user's profile with saved details
    else:
        form = EditProfileForm(initial={'bio': user_profile.bio, 'birthday': user_profile.birthday})
    
    context = {'form': form}
    return render(request, 'friendlist/edit_profile.html', context)
