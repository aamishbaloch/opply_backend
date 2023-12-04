from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at')


admin.site.register(Order, OrderAdmin)
