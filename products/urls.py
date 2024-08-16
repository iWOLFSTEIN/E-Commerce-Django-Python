from django.urls import path

from products import views


urlpatterns = [
    path("get_products", views.Products.as_view()),
    path("add_product", views.Products.as_view()),
    path("add_review/<int:product_id>", views.ProductReviews.as_view()),
]
