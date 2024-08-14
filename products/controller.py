from app_auth.controller import verify_jwt_token, get_error_response
from products.models import Product
from products.serializer import ProductReviewSerializer, ProductSerializer
from rest_framework.response import Response


class ProductsController:
    @verify_jwt_token
    def add_product(request, *args, **kargs):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return get_error_response(serializer.errors, status=400)

        product = serializer.save()
        return Response(
            {"productId": product.id, "message": "Product created successfully"},
            status=200,
        )


class ProductReviewsController:
    @verify_jwt_token
    def add_review(request, *args, **kargs):
        product_id = kargs.get("product_id")
        try:
            product = Product.objects.get(id=product_id)
        except Exception as _:
            return Response({"error": "Product not found"}, status=404)

        data = request.data.copy()
        data["product"] = product.id

        serializer = ProductReviewSerializer(data=data)
        if not serializer.is_valid():
            return get_error_response(serializer.errors, status=400)

        review = serializer.save()
        return Response(
            {
                "reviewId": review.id,
                "productId": product.id,
                "message": "Review added to product successfully",
            },
            status=200,
        )
