from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from . import serializers, services, models, filters


class ProductByCategoryView(ViewSet):
    def retrieve(self, request, pk=None):
        categories_service = services.CategoryServiceV1()
        queryset = categories_service.get_categories('GET').all()
        category_try = get_object_or_404(queryset, pk=pk)
        serializer = serializers.CategorySerializer(category)
        serializer.is_valid(raise_exception=True)
        category = serializer.se

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
