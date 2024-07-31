from django.contrib import admin

from app_auth.models import Login, User

admin.site.register(User)
admin.site.register(Login)
