from rest_framework.views import APIView

from products.controller import ProductReviewsController, ProductsController
from rest_framework.response import Response
from .controller import CustomPagination


class Products(APIView):
    pagination_class = CustomPagination

    def get(self, request, *args, **kargs):
        return ProductsController.get_products(request, *args, **kargs)

    def post(self, request, format=None):
        return ProductsController.add_product(request)


class ProductReviews(APIView):
    def post(self, request, *args, **kargs):
        product_id = kargs.get("product_id")
        if not product_id:
            return Response({"error": "Product id is missing"}, status=400)
        return ProductReviewsController.add_review(request, product_id=product_id)
