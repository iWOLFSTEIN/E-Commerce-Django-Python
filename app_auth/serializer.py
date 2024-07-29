from app_auth.models import Login, Signup
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")

    class Meta:
        model = Signup
        fields = ["email", "password", "firstName", "lastName"]
        extra_kwargs = {"password": {"write_only": True}}


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
