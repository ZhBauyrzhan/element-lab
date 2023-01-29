from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers, services, models, filters

class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.prefetch_related('product').all()
    serializer_class = serializers.CategorySerializer
    filter_class = filters.CategoryFilter


class ProductViewSet(ModelViewSet):
    product_services = services.ProductServiceV1
    serializer = serializers.ProductSerializer
    filter_class = filters.ProductFilter

    def get_queryset(self):
        return self.product_services.get_products()

    def create_product(self, serializer: serializers.ProductSerializer):
        self.product_services.create_product(data=serializer.validated_data)
