from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    """
    Allows adding/editing line items directly within the Order admin page
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for Order model
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total',
              'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)