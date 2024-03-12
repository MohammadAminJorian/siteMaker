from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from knox import views as knox_views

app_name = 'account'
urlpatterns = [
    path('api/', Home.as_view(), name='home'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/profile', ProfileView.as_view(), name='profileView'),
    path('api/updateProfile/<int:pk>', UpdateProfile.as_view(), name='updateProfile'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),



]