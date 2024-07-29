from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Signup(AbstractUser):
    password = models.CharField(max_length=128)
    email = models.EmailField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    REQUIRED_FIELDS = ["email", "password", "first_name", "last_name"]
    USERNAME_FIELD = "email"


class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)
