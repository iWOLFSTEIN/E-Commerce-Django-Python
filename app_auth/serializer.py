from app_auth.models import Login, OtpVerification, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")

    class Meta:
        model = User
        fields = ["id", "email", "password", "firstName", "lastName"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = super().create(validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class OtpVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtpVerification
        fields = "__all__"
