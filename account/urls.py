from .views import *
from django.urls import path
from .Serializer import *


app_name='account'

urlpatterns = [
    path('login/', UserLoginView.as_view() ,name='login'),
]