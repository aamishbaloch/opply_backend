from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Customer


class CustomerAdmin(UserAdmin):
    list_display = ("username",)
    fieldsets = (
        (_('Personal Info'), {
            'fields': (
                'username', 'first_name', 'last_name'
            )
        }),
        (_('Permissions Info'), {'fields': ('is_active',)}),
        (_('Important dates'), {'fields': ('last_login',)}),
        ('Password Info', {'fields': ('password',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'first_name', 'last_name', 'password1', 'password2')}
         ),
    )

    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(Customer, CustomerAdmin)
