"""checkout admin"""
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    """class docstring """
    model = OrderItem
    readonly_fields = ('order_item_total',)


class OrderAdmin(admin.ModelAdmin):
    """order admin doc string"""

    ordering = ('-date',)

    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_nbr', 'grand_total',
                       'total', 'date', 'delivery',)

    list_display = ('order_nbr', 'full_name', 'date',
                    'grand_total', 'total', 'delivery',)

    fields = ('user_account', 'order_nbr', 'full_name', 'phone_nbr',
              'address_line_one', 'address_line_two', 'city',
              'county', 'postcode', 'country',
              'date', 'delivery', 'total',
              'grand_total', 'email',)


admin.site.register(Order, OrderAdmin)
