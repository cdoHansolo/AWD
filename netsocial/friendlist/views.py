from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here

def home_view(request):
    return render(request, 'friendlist/homepage.html')

def register_view(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('profile')
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
    context = {'user':user}
    return render(request, 'friendlist/profilepage.html', context)
