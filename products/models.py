from django.db import models

from rest_framework.pagination import PageNumberPagination


class Product(models.Model):
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discountPercentage = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    thumbnail = models.ImageField()

    pagination_class = PageNumberPagination


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField()
    reviewerName = models.CharField(max_length=256)

    pagination_class = PageNumberPagination
