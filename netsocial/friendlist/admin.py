from django.contrib import admin
from .models import FriendRequest
from .models import UserProfile
from .models import Friend
from .models import Post

# Register your models here.
admin.site.register(FriendRequest)
admin.site.register(UserProfile)
admin.site.register(Friend)
admin.site.register(Post)