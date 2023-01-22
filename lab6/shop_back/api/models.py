from django.db import models


# Create your models here.
class Product(models.Model):
    name: models.CharField(max_length=20)
    cost: models.FloatField()
    description: models.TextField()
    amount: models.IntegerField()
    is_active: models.BooleanField()


class Category(models.Model):
    name: models.CharField(max_length=100)
