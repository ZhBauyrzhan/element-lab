from typing import Protocol, OrderedDict

from django.db.models import QuerySet

from shop_back.api import models, repos


class CategoryServiceInterface(Protocol):
    category_repos: repos.CategoryReposInterface

    def create_category(self, data: OrderedDict) -> None:
        ...

    def get_categories(self, action: str) -> QuerySet[models.Category]:
        ...

    def delete_category(self, category: models.Category) -> None:
        ...


class CategoryServiceV1:
    category_repos: repos.CategoryReposInterface = repos.CategoryReposV1()

    def create_category(self, data: OrderedDict) -> None:
        try:
            self.category_repos.create_category(data=data)
        except Exception as e:
            print('Error in category service v1 during create operation', e)

    def get_categories(self, action: str) -> QuerySet[models.Category]:
        return self.category_repos.get_category()

    def delete_category(self, category: models.Category) -> None:
        try:
            self.category_repos.delete_category(category=category)
        except Exception as e:
            print('Error in category service v1 during delete category', e)


class ProductServiceInterface(Protocol):
    protocol_repos: repos.ProductReposInterface

    def create_product(self, data: OrderedDict) -> None: ...

    def get_products(self, action: str) -> QuerySet[models.Product]: ...

    def delete_product(self, product: models.Product) -> None: ...


class ProductServiceV1:
    protocol_repos: repos.ProductReposInterface = repos.ProductReposV1()

    def create_product(self, data: OrderedDict) -> None:
        try:
            self.protocol_repos.create_product(data=data)
        except Exception as e:
            print(e)

    def get_products(self, action: str) -> QuerySet[models.Product]:
        return self.protocol_repos.get_products()

    def delete_product(self, product: models.Product) -> None:
        try:
            self.protocol_repos.delete_product(product=product)
        except Exception as e:
            print(e)
