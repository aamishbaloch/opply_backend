from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomerManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        extra_fields.update({
            "is_staff": False,
            "is_superuser": False,
            "is_active": False,
        })

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        raise ValueError(_("Customer cannot be a superuser"))
