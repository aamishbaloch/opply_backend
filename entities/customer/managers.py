from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _


class CustomerManager(UserManager):

    def _create_user(self, username, email, password, **extra_fields):
        extra_fields.update({
            "is_staff": False,
            "is_superuser": False,
            "is_active": False,
        })

        return super(CustomerManager, self)._create_user(username, email, password, **extra_fields)

    def create(self, **obj_data):
        obj_data.update({
            "is_staff": False,
            "is_superuser": False,
            "is_active": False,
        })
        return super(CustomerManager, self).create(**obj_data)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        raise ValueError(_("Customer cannot be a superuser"))
