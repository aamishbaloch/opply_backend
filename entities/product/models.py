from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from entities.product.managers import ProductManager


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    quantity = models.PositiveIntegerField(default=0)

    objects = ProductManager()

    def __str__(self):
        return self.name

    def is_available(self, required_quantity):
        return True if self.quantity >= required_quantity else False

    def sell_if_available(self, required_quantity):
        if not self.is_available(required_quantity):
            return False
        self.quantity -= required_quantity
        self.save()
        return True

