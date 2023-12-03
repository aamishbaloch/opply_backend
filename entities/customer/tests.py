from django.test import TestCase

from .models import Customer


class CustomerTestCase(TestCase):
    def setUp(self):
        pass

    def test_customer_cannot_be_a_staff_user(self):
        params = {
            'username': 'Zohaan',
            'password': 'aamish',
            'is_staff': True,
        }

        customer = Customer.objects.create(**params)

        self.assertEqual(customer.username, 'Zohaan')
        self.assertFalse(customer.is_staff)

    def test_customer_cannot_be_a_super_user(self):
        params = {
            'username': 'Zohaan',
            'password': 'aamish',
            'is_superuser': True,
        }

        customer = Customer.objects.create(**params)

        self.assertEqual(customer.username, 'Zohaan')
        self.assertFalse(customer.is_staff)
