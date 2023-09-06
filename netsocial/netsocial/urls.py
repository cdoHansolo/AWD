from django.contrib import admin
from django.urls import path
from friendlist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='registration_view'),
    path('registration_success/', views.registration_success, name='registration_success'),
]
