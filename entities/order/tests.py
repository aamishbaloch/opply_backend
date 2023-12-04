from django.test import TestCase

from django.db import IntegrityError

from .models import Order, OrderItem
from ..customer.models import Customer
from ..product.models import Product


class OrderTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(username='Zohaan', password='password')

        self.products = [
            Product.objects.create(name='Milk', quantity=5, price=10.99),
            Product.objects.create(name='Sugar', quantity=3, price=3.99),
        ]

    def test_order_creation(self):
        params = {
            'customer': self.customer,
        }

        order = Order.objects.create(**params)

        self.assertEqual(order.customer.id, self.customer.id)
        self.assertEqual(order.items.count(), 0)

    def test_order_creation_with_items(self):
        params = {
            'customer': self.customer,
        }

        order = Order.objects.create(**params)

        params = [
            {
                'product': self.products[0],
                'buying_price': self.products[0].price,
                'quantity': 2
            },
            {
                'product': self.products[1],
                'buying_price': self.products[1].price,
                'quantity': 2
            }
        ]

        order_items = OrderItem.objects.bulk_create([
            OrderItem(**params[0]),
            OrderItem(**params[0]),
        ])

        for item in order_items:
            order.items.add(item)

        self.assertEqual(order.customer.id, self.customer.id)
        self.assertEqual(order.items.count(), 2)
