from app_auth.models import Login, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")

    class Meta:
        model = User
        fields = ["email", "password", "firstName", "lastName"]
        extra_kwargs = {"password": {"write_only": True}}


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
