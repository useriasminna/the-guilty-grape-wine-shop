"""
Vouchers App - Admin
----------------
Admin configuration for Vouchers App.
"""
from django.contrib import admin

from .models import Voucher


class VouchersAdmin(admin.ModelAdmin):
    """Class for displaying vouchers in admin panel"""

    list_display = (
        'voucher_code',
        'percentage',
        'user',
    )


admin.site.register(Voucher, VouchersAdmin)
