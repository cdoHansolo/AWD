from django.contrib import admin
from django.urls import path
from friendlist import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('send_friend_request/<int:receiver_id>/', views.send_friend_request, name='send_friend_request'),
    path('view_friend_requests/', views.view_friend_requests, name='view_friend_requests'),
    path('accept_friend_request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('reject_friend_request/<int:request_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('remove_friend/<int:friend_id>/', views.remove_friend, name='remove_friend'),
    # path('friends/<int:friend_id', views.friend_page, name='friend_page'),
    path('friendpage/', views.friends_page_view, name='friend_page_view'),
    path('create_post/', views.create_post, name='create_post'),
    

]
