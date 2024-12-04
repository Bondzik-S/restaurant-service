from django.conf import settings
from django.db import models

from accounts.models import Cook


class DishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    def __str__(self):
        return self.name
