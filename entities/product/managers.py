from django.db import models, IntegrityError


class ProductManager(models.Manager):
    def create(self, **obj_data):
        if obj_data.get('price', None):
            if not obj_data.get('price') > 0:
                raise IntegrityError

        return super().create(**obj_data)
