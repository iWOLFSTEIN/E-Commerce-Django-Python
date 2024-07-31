from functools import wraps

import jwt
from app_auth.models import User
from app_auth.serializer import LoginSerializer, UserSerializer
from rest_framework.response import Response
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken


def verifyJwtToken(func):
    @wraps(func)
    def decorator(request):
        token = str(request.auth)
        try:
            payload = jwt.decode(
                jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"]
            )
            user = User.objects.get(id=payload["id"])
            if not user.is_active:
                user.is_active = True
                user.save()
            return func(request, user)
        except jwt.ExpiredSignatureError as e:
            print(e)
            return Response({"error": "Activations link expired"}, status=400)
        except jwt.exceptions.DecodeError as e:
            print(e)
            return Response({"error": "Invalid Token"}, status=400)

    return decorator


def get_tokens_for_user(user) -> str:
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


def get_error_response(errors, status):
    error = "Unknown error"
    for key, value in errors.items():
        if value[0].code == "required":
            value = value[0].__str__()[5:]
            error = "{} {}".format(key, value)
        elif value[0].code == "invalid":
            error = value[0].__str__()
        break

    response_body = {"error": error}
    return Response(response_body, status=status)


class Auth:
    def register(request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=200)
        else:
            return get_error_response(serializer.errors, status=400)

    def login(request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return get_error_response(serializer.errors, status=400)
