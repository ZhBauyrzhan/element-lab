from django.db.models import QuerySet, Q
from django_filters import rest_framework as filters
from . import models


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = models.Category
        fields = '__all__'

    def name_filter(self, queryset: QuerySet[models.Category], _, value):
        return queryset.filter(
            name__icontains=value
        )


class ProductFilter(filters.FilterSet):
    name: filters.CharFilter(field_name='name', lookup_expr='icontains')
    price = filters.NumberFilter(field_name='price', lookup_expr=' ')

    class Meta:
        model = models.Product
        fields = '__all__'
