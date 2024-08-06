from django.contrib import admin

from app_auth.models import Login, User, UserVerification
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)
admin.site.register(Login)
admin.site.register(UserVerification)
