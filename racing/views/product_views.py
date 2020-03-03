from racing.base.base_views import PrivatePostAPIView, PrivateGetAPIView
from racing.constants import Result
from racing.mangers import product_manager
from racing.models import Product
from racing.serializers import CreateProductSerializer, GetPersonalProductListSerializer


class CreateProductView(PrivatePostAPIView):
    serializer_class = CreateProductSerializer

    def process(self, data):
        self.validate_data(data)
        product = Product.objects.create(
            user_id=self.user_id,
            name=data["name"],
            description=data.get("description", ""),
            price=data.get("price", 0.0),
            accessory_id=data["accessory_id"]
        )

        product_response = product_manager.generate_product_response(product)
        product_response = product_manager.fill_accessory_info([product_response])

        return Result.SUCCESS, product_response

    def validate_data(self, data):
        pass


class GetPersonalProductListView(PrivateGetAPIView):
    serializer_class = GetPersonalProductListSerializer

    def process(self, data):
        products = list(Product.objects.filter(user_id=self.user_id))
        product_response_list = []
        for p in products:
            product_response = product_manager.generate_product_response(p)
            product_response_list.append(product_response)

        product_response_list = product_manager.fill_accessory_info(product_response_list)
        product_response_list = product_manager.fill_image_info(product_response_list)

        return Result.SUCCESS, product_response_list
