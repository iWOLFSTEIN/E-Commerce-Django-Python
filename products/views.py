from rest_framework.views import APIView

from controller import ProductsController


class Products(APIView):
    def post(self, request, format=None):
        return ProductsController.add_product(request)
