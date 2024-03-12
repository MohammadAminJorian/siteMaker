from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')
