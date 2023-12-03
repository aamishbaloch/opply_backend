from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .managers import CustomerManager

User = get_user_model()


class Customer(User):
    objects = CustomerManager()

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
