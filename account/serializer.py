from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'phone', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'phone', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['email'], validated_data['username'], validated_data['phone'],
                                          validated_data['password'])
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'nationality_code', 'address', 'photo')


class ProfileUppdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'nationality_code', 'address', 'photo')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        if profile_data is not None:
            instance.profile.first_name = profile_data['first_name']
            instance.profile.last_name = profile_data['last_name']
            instance.profile.nationality_code = profile_data['nationality_code']
            instance.profile.address = profile_data['address']
            instance.profile.photo = profile_data['photo']
            instance.profile.save()
        return super().update(instance, validated_data)




class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['admin', 'category', 'image', 'title', 'slug', 'desc', 'time_of_create' , 'price' , 'Language_of_create', 'status']


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['admin', 'category', 'image', 'title', 'slug', 'desc', 'time_of_create' , 'price' , 'Language_of_create', 'status']

    def update(self, instance, validated_data):
        post_data = validated_data.pop('postupdate', None)
        if post_data is not None:
            instance.postupdate.admin = post_data['admin']
            instance.postupdate.category = post_data['category']
            instance.postupdate.image = post_data['image']
            instance.postupdate.title = post_data['title']
            instance.postupdate.slug = post_data['slug']
            instance.postupdate.desc = post_data['desc']
            instance.postupdate.time_of_create = post_data['time_of_create']
            instance.postupdate.price = post_data['price']
            instance.postupdate.Language_of_create = post_data['Language_of_create']
            instance.postupdate.status = post_data['status']
            instance.postupdate.save()
        return super().update(instance, validated_data)


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'status', 'position']

    class Meta:
        model = Category
        fields = "__all__"



class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'post', 'quantity', 'is_paid']

