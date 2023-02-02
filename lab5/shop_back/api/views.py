from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from . import serializers, services, models, filters
from .models import Product


class ProductByCategoryView(ViewSet):
    def retrieve(self, request, pk=None):
        resp = serializers.ProductSerializer(Product.objects.filter(category__pk=pk), many=True)
        return Response(resp.data)

class CategoryViewSet(ModelViewSet):
    print('WAAAAAAAAAAAAAAAAS1')
    categories_service = services.CategoryServiceV1()
    queryset = categories_service.get_categories('GET')
    serializer_class = serializers.CategorySerializer
    filter_class = filters.CategoryFilter

    def perform_create(self, serializer):
        self.categories_service.create_category(serializer.validated_data)


class ProductViewSet(ModelViewSet):
    product_service = services.ProductServiceV1()
    queryset = product_service.get_products('GET')
    serializer_class = serializers.ProductSerializer
    filter_class = filters.ProductFilter

    def perform_create(self, serializer):
        print(serializer.validated_data)
        self.product_service.create_product(serializer.validated_data)
