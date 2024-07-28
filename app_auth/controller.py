from app_auth.serializer import LoginSerializer, SignupSerializer
from rest_framework.response import Response


def get_error_response(errors, status):
    for key, value in errors.items():
        value = value[0].__str__()[5:]
        error = "{} {}".format(key, value)

    response_body = {"error": error}
    return Response(response_body, status=status)


class Auth:
    def register(request):
        serializer = SignupSerializer(data=request.data)

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
