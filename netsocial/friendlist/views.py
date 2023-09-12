from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


from .models import UserProfile
from .models import FriendRequest
from .models import Friend
from .models import Post


from .forms import RegisterForm
from .forms import EditProfileForm
from .forms import FriendRequestForm
from .forms import PostForm

# Create your views here

def home_view(request):
    users = User.objects.all() #Get users from database
    print("Is user authenticated?", request.user.is_authenticated)
    return render(request, 'friendlist/homepage.html', {'users': users})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # print(form.is_valid + "validity")
        if form.is_valid():
            email = form.cleaned_data['email']
            # print(email+ "email")

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

def logout_view(request):
    logout(request)
    return redirect('home')

def profile_view(request, username=None):
    if username is None:
        user = request.user
        print("Is user authenticated?", request.user.is_authenticated)
    else:
        user = get_object_or_404(User, username=username)
        print("Is user authenticated?", request.user.is_authenticated)

    is_friend = False
    request_sent = False

    if request.user.is_authenticated and request.user != user:
        is_friend = request.user.friends.filter(friend=user).exists()

    user_posts = Post.objects.filter(user=user)

    context = {
                'user': user,
                'is_friend': is_friend, #passing to template
                'request_sent': request_sent,
                'user_posts':user_posts
              }
    return render(request, 'friendlist/profilepage.html', context)

def edit_profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    print(user_profile)

    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']
            
            user_profile.bio = bio
            print(user_profile.bio)
            user_profile.birthday = birthday
            user_profile.save()

            return redirect('profile') #redirect back to user's profile with saved details
    else:
        form = EditProfileForm(initial={'bio': user_profile.bio, 'birthday': user_profile.birthday})
    
    context = {'form': form}
    return render(request, 'friendlist/edit_profile.html', context)

@login_required
def send_friend_request(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    friend_request = FriendRequest(sender=request.user, receiver=receiver, status='pending')
    friend_request.save()
    return redirect('profile_view', username=receiver.username)

def view_friend_requests(request):
    #get friend requests
    friend_requests = FriendRequest.objects.filter(receiver=request.user, status='pending')
    context = {
        'friend_requests': friend_requests,
    }

    return render(request, 'friendlist/view_friend_requests.html', context)

def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if friend_request.receiver == request.user and friend_request.status == 'pending':
        friend_request.status = 'accepted'
        friend_request.save()
        Friend.objects.create(user=friend_request.sender, friend=friend_request.receiver)
        Friend.objects.create(user=friend_request.receiver, friend=friend_request.sender)

    
    friend_requests = FriendRequest.objects.filter(receiver=request.user, status='pending')
    context = {
        'friend_requests': friend_requests,
    }
    
    return render(request, 'friendlist/friendpage.html', context)

def reject_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if friend_request.receiver == request.user and friend_request.status == 'pending':
        friend_request.status = 'rejected'
        friend_request.save()
    friend_requests = FriendRequest.objects.filter(receiver=request.user, status='pending')
    context = {
        'friend_requests': friend_requests,
    }
    
    return render(request, 'friendlist/friendpage.html', context)

def remove_friend(request, friend_id):
    friend = get_object_or_404(User, id=friend_id)
    Friend.objects.filter(user=request.user, friend=friend).delete()
    return redirect('profile_view', username=friend.username)


# def friends_page_view(request):
#     #get friend requests
#     friend_requests = FriendRequest.objects.filter(receiver=request.user, status='pending')
#     context = {
#         'friend_requests': friend_requests,
#     }
    
#     return render(request, 'friendlist/friendpage.html', context)

def friends_page_view(request):
    #get friend requests
    friend_requests = FriendRequest.objects.filter(receiver=request.user, status='pending')
    friends = Friend.objects.filter(user=request.user)

    context = {
        'friend_requests': friend_requests,
        'friends':friends
    }
    return render(request, 'friendlist/friendpage.html', context)



def create_post(request):
    print("request")
    if request.method == 'POST':
        print("POST WORKS")
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile_view', username=request.user.username)  # Redirect to the user's profile page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


