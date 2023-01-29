import serializers as serializers
from rest_framework import serializers

from .import models


class _CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        field = ('id', 'name', 'price', 'amount')


class _ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        category = models.Category
        field = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # category = models.Category
    class Meta:
        model = models.Product
        fields = '__all__'
