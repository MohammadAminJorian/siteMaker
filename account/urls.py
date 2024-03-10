from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'myuser'
urlpatterns = [
    path('login/', Login, name="login"),
 ]