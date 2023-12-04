from django.test import TestCase

from django.db import IntegrityError

from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        pass

    def test_product_creation(self):
        params = {
            'name': 'Milk',
            'price': 10.99,
            'quantity': 5,
        }

        product = Product.objects.create(**params)

        self.assertEqual(product.name, 'Milk')
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.quantity, 5)

    def test_quantity_cannot_be_less_than_zero(self):
        params = {
            'name': 'Milk',
            'price': 10.99,
            'quantity': -5
        }

        with self.assertRaises(IntegrityError):
            Product.objects.create(**params)

    def test_quantity_default_is_zero(self):
        params = {
            'name': 'Milk',
            'price': 10.99,
        }

        product = Product.objects.create(**params)

        self.assertEqual(product.quantity, 0)

    def test_price_cannot_be_less_than_zero(self):
        params = {
            'name': 'Milk',
            'quantity': 5
        }

        with self.assertRaises(IntegrityError):
            Product.objects.create(**params)

        params = {
            'name': 'Milk',
            'quantity': 5,
            'price': -7.99,
        }

        with self.assertRaises(IntegrityError):
            Product.objects.create(**params)

    def test_is_available(self):
        params = {
            'name': 'Milk',
            'quantity': 5,
            'price': 10.99,
        }

        product = Product.objects.create(**params)

        self.assertTrue(product.is_available(3))
        self.assertFalse(product.is_available(8))

    def test_sell_if_available(self):
        params = {
            'name': 'Milk',
            'quantity': 5,
            'price': 10.99,
        }

        product = Product.objects.create(**params)

        self.assertTrue(product.sell_if_available(3))
        self.assertFalse(product.sell_if_available(3))
        self.assertTrue(product.sell_if_available(1))
