from django.urls import path

from app_auth import views


urlpatterns = [
    path("signup", views.Signup.as_view()),
    path("login", views.Login.as_view()),
    path("otp", views.Otp.as_view()),
]
