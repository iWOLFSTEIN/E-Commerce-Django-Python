from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.CharField(max_length=256, unique=True, null=False)
    password = models.CharField(null=False, max_length=128, min_length=6)
    name = models.TextField(null=False, max_length=256)

    REQUIRED_FIELDS = [email, password, name]
    USERNAME_FIELD = "email"


