from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from . import models


class CategoryReposInterface(Protocol):
    def create_category(self, data: OrderedDict) -> models.Category: ...

    def get_category(self) -> QuerySet[models.Category]: ...

    def delete_category(self, category: models.Category) -> None: ...


class CategoryReposV1:

    def create_category(self, data: OrderedDict) -> models.Category:
        print(**data)
        return models.Category.objects.create(**data)

    def get_categories(self) -> QuerySet[models.Category]:
        return models.Category.objects.all()

    def delete_category(self, category: models.Category) -> None:
        category.delete()


class ProductReposInterface(Protocol):
    def create_product(self, data: OrderedDict) -> models.Product: ...

    def get_products(self) -> QuerySet[models.Product]: ...

    def delete_product(self, product: models.Product) -> None: ...


class ProductReposV1:
    def create_product(self, data: OrderedDict) -> models.Product:
        return models.Category.objects.create(**data)

    def get_products(self) -> QuerySet[models.Product]:
        return models.Category.objects.all()

    def delete_product(self, product: models.Product) -> None:
        product.delete()
