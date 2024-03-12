from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'phone' ,'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username','phone', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['email'] , validated_data['phone'] , validated_data['username'], validated_data['password'] , is_admin = False)
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
