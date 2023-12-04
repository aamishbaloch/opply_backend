from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from entities.customer.models import Customer
from entities.product.models import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.RESTRICT)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='customers', on_delete=models.RESTRICT)
    items = models.ManyToManyField(OrderItem)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.username




