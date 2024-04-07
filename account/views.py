import json
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework import viewsets
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import *
from .models import MyUser , Category , Post
from django.db.models import Q
from django.contrib.auth import logout
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.renderers import TemplateHTMLRenderer



class RegisterAPI(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs ):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)




class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': "Logout successful"})

class ProfileView(APIView):
    def get(self, request):
        profile = Profile.objects.get(user_id=request.user.id)

        return JsonResponse({
            'id': profile.id,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'nationality_code': profile.nationality_code,
            'address': profile.address,
            'photo': profile.photo.url,
        }, status=status.HTTP_200_OK)


class UpdateProfile(RetrieveUpdateAPIView):
    serializer_class = ProfileUppdateSerializer
    queryset = Profile.objects.all()




class Home(APIView):
    def get(self, request):
        return Response({
            None
        })


#
# class category(APIView):
#     # def get(self, request, format=None):
#     #     data = Category.objects.all().values()
#     #     return Response(data)
#
#     def post(self, request, *args, **kwargs):
#         data = {
#             'title': request.data.get('title'),
#             'image': request.data.get('image'),
#             'status': request.data.get('status')
#         }
#         serializer = Category(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )




class categoryView(APIView):
    def get(self, request, id):
        data = get_object_or_404(Category, id=id, status=True)

        return JsonResponse({
            'id': data.id,
            'title': data.title,
            'status': data.status,
            'position': data.position,
        }, status=status.HTTP_200_OK)


class categoryCreate(APIView):

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CreateCategorySerializer(category, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data

        serializer = CreateCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class postView(APIView):
    def get(self, request, id):
        data = get_object_or_404(Post, id=id, status=publish)
        return JsonResponse({
            'id': data.id,
            'title': data.title,
            'slug': data.slug,
            'desc': data.desc,
            'image': data.image.url,
            'status': data.status,
            'publish': data.publish,
            'admin': data.admin,
        }, status=status.HTTP_200_OK)

class postCreate(APIView):

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostCreateSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        data = request.data
        serializer = PostCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# https://forum.djangoproject.com/t/create-a-book-instance-with-multiple-tags-in-django-rest-framework/19284
