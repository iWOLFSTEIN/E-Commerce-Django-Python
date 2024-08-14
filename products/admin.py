from django.contrib import admin

from products.models import Product, ProductReview

admin.site.register(Product)
admin.site.register(ProductReview)
