from functools import wraps

from celery import shared_task
import jwt
from app_auth.models import User, UserVerification
from app_auth.serializer import LoginSerializer, UserSerializer
from rest_framework.response import Response
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
import pyotp
from datetime import datetime, timedelta


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


def get_token_for_user(user) -> str:
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


def verify_user(user: User):
    user_verification = UserVerification(user=user)
    user_verification.otp = int(
        generate_otp(user=user, user_verification=user_verification)
    )
    user_verification.next_possible_attempt = datetime.now() + timedelta(
        seconds=((user_verification.otp_attempt_counter + 1) * 30)
    )
    user_verification.secret_key = pyotp.random_base32()
    user_verification.save()
    send_otp_email.delay(user.id, user_verification.otp)


def generate_otp(user: User, user_verification: UserVerification):
    hotp = pyotp.HOTP(user_verification.secret_key)
    otp = hotp.at(user_verification.otp_attempt_counter)
    return otp


@shared_task
def send_otp_email(userId: str, otp: int):
    user = User.objects.get(id=userId)
    user.email_user(
        "Account Verification",
        otp_email_body(name=user.name(), otp=otp),
        "XYZ Verification <{}>".format(settings.EMAIL_HOST_USER),
    )


def otp_email_body(name: str, otp: int) -> str:
    return """Dear {},

Thank you for registering with XYZ. To complete your account verification, please use the following One-Time Password (OTP):

Your OTP Code: {} 

Please enter this code in the verification section of our website/app to complete your account setup.

If you did not initiate this request, please ignore this email or contact our support team immediately.

Best regards,

The XYZ Team

+12 345 6789012
xyz@xyz.com
""".format(
        name, otp
    )


def get_error_response(errors, status):
    print(errors)
    error = "Unknown error"
    for key, value in errors.items():
        if value[0].code == "required":
            value = value[0].__str__()[5:]
            error = "{} {}".format(key, value)
        else:
            error = value[0].__str__()
        break

    response_body = {"error": error}
    return Response(response_body, status=status)


class Auth:
    def register(request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = get_token_for_user(user)
            try:
                verify_user(user=user)
                pass
            except Exception as e:
                print(e)
            return Response(
                {
                    "user": UserSerializer(user).data,
                    "token": token,
                    "message": "Success!",
                },
                status=200,
            )
        else:
            return get_error_response(serializer.errors, status=400)

    def login(request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return get_error_response(serializer.errors, status=400)

        user = User.objects.get(email=serializer.data.get("email"))
        if not user:
            return Response({"error": "User does not exist!"}, status=404)

        token = get_token_for_user(user)
        return Response(
            {
                "user": UserSerializer(user).data,
                "token": token,
                "message": "Success!",
            },
            status=200,
        )
