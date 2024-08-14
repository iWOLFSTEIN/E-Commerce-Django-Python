from app_auth.controller import verify_jwt_token


class ProductsController:
    @verify_jwt_token
    def add_product(request, user):
        pass
