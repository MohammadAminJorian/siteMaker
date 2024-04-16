from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from knox import views as knox_views
import requests


app_name = 'account'
urlpatterns = [
    path('api/', Home.as_view(), name='home'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/profile', ProfileView.as_view(), name='profileView'),
    path('api/updateprofile/<int:pk>', UpdateProfile.as_view(), name='updateProfile'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/logout/', LogoutView.as_view(), name='LogoutView'),
    path('api/viewpost/', postView.as_view(), name='postView'),
    path('api/postCreate/', postCreate.as_view(), name='postCreate'),
    path('api/UpdatePost/<int:pk>', UpdatePost.as_view(), name='UpdatePost'),
    path('api/categoryView/<int:id>', categoryView.as_view(), name='categoryCreate'),
    path('api/categoryCreate/', categoryCreate.as_view(), name='categoryCreate'),

]