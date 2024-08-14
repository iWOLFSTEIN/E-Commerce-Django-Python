from django.urls import path

from app_auth import views


urlpatterns = [
    path("add_product", views.Signup.as_view()),
]
