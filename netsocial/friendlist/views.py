from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register_view(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() #save user details and log user in

            return redirect('registration_success')