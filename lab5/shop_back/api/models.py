from django.db import models


class Category(models.Model):
    name: models.CharField(max_length=100)
    created_at: models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Category: {self.name=}'


class Product(models.Model):
    name: models.CharField(max_length=100)
    price: models.FloatField()
    description: models.TextField()
    amount: models.IntegerField()
    is_active: models.BooleanField()
    category: models.ForeignKey(
        to=Category,
        on_delete=models.PROTECT,
        related_name='products'
    )
    created_at: models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField(auto_now=True)
