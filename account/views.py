from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from .models import *
from .Serializer import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['phone'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
