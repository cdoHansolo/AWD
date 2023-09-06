from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register_view(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('registration_success')
    else:
        form = RegisterForm()
    
    return render(request, 'friendlist/register_form.html', {'form': form})