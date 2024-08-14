from rest_framework.views import APIView
from app_auth.controller import Auth


class Signup(APIView):
    def post(self, request, format=None):
        return Auth.register(request)


class Login(APIView):
    def post(self, request, format=None):
        return Auth.login(request)


class Otp(APIView):
    def post(self, request, format=None):
        return Auth.verify_otp(request)

    def get(self, request, format=None):
        return Auth.request_otp(request)
