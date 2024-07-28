from rest_framework.views import APIView
from app_auth.controller import Auth


class Signup(APIView):
    def post(self, request, format=None):
        return Auth.register(request)


class Login(APIView):
    def post(self, request, format=None):
        return Auth.login(request)
