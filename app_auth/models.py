import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from app_auth.managers import UserManager


class User(AbstractUser):
    id = models.CharField(default=uuid.uuid4().hex, max_length=24, primary_key=True)
    username = None
    password = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150, null=False, blank=False)
    last_name = models.CharField(max_length=150, null=False, blank=False)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = self.email
        super().save(*args, **kwargs)

    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self) -> str:
        return self.email


class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=False, blank=False)


class UserVerification(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    otp = models.IntegerField(default=-111111)
    otp_attempt_counter = models.IntegerField(default=-1)
    next_possible_attempt = models.DateTimeField()
    secret_key = models.CharField(max_length=32, default="")


class OtpVerification(models.Model):
    otp = models.IntegerField()
