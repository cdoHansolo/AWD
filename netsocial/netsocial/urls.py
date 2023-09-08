from django.contrib import admin
from django.urls import path
from friendlist import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
]
