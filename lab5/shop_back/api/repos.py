from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from . import models


class CategoryReposInterface(Protocol):

    @staticmethod
    def create_category(data: OrderedDict) -> models.Category: ...

    @staticmethod
    def get_categories() -> QuerySet[models.Category]: ...

    @staticmethod
    def delete_category(category: models.Category) -> None: ...


class CategoryReposV1:

    @staticmethod
    def create_category(data: OrderedDict) -> models.Category:
        print('CATEGORY REPOS CREATE')
        print(data)
        return models.Category.objects.create(**data)

    @staticmethod
    def get_categories() -> QuerySet[models.Category]:
        print('CATEGORY REPOS GET')
        return models.Category.objects.all()

    @staticmethod
    def get_products_by_category(data: OrderedDict) -> QuerySet[models.Category]:
        print('PRODUCTS BY CATEGORY GET')
        return models.Category.objects.all().prefetch_related('pr')

    @staticmethod
    def delete_category(category: models.Category) -> None:
        category.delete()


class ProductReposInterface(Protocol):
    @staticmethod
    def create_product(data: OrderedDict) -> models.Product: ...

    @staticmethod
    def get_products() -> QuerySet[models.Product]: ...

    @staticmethod
    def delete_product(product: models.Product) -> None: ...


class ProductReposV1:
    @staticmethod
    def create_product(data: OrderedDict) -> models.Product:
        return models.Product.objects.create(**data)

    @staticmethod
    def get_products() -> QuerySet[models.Product]:
        return models.Product.objects.all()

    @staticmethod
    def delete_product(product: models.Product) -> None:
        product.delete()
